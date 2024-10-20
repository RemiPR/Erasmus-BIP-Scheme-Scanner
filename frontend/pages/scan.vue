<template>
  <div class="h-screen flex items-center justify-center bg-gradient-to-r from-[#4dbed2] to-[#4f46e5] px-4 relative font-sans">
    <div class="relative flex">
      <div class="relative">
        <video
          ref="video"
          autoplay
          muted
          playsinline
          class="w-[640px] h-[480px] border-2 border-black shadow-lg mr-5"
        ></video>
        <canvas ref="canvas" class="absolute top-0 left-0"></canvas>
      </div>
      <div
        id="detected-items"
        class="w-[320px] bg-white border border-gray-300 p-2.5 max-h-[480px] overflow-y-auto shadow-md"
      >
        <h2 class="text-center mb-2.5 text-xl">Detected Objects</h2>
        <ul class="list-none p-0">
          <li
            v-for="(item, index) in detectedItemsArray"
            :key="index"
            class="p-2 border-b border-gray-300 text-base"
          >
            {{ item.name }} - {{ item.confidence }}% confidence
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>

useHead({
  script: [
    {
      src: 'https://cdn.roboflow.com/0.2.26/roboflow.js',
      async: true,
    },
  ],
});

const video = ref(null);
const canvas = ref(null);
const detectedItems = reactive(new Map());
let ctx = null;
let model = null;

const detectedItemsArray = computed(() =>
  Array.from(detectedItems.entries()).map(([key, value]) => ({
    name: key,
    confidence: value.confidence,
  }))
);

onMounted(() => {
  // Wait until Roboflow is loaded
  const checkRoboflow = setInterval(() => {
    if (window.roboflow) {
      clearInterval(checkRoboflow);
      initializeApp();
    }
  }, 100);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', resizeCanvas);
});

const initializeApp = async () => {
  await startVideoStream();
  await loadModel();
  detectFrame();
  window.addEventListener('resize', resizeCanvas);
};

const startVideoStream = async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: false,
      video: {
        facingMode: 'environment',
      },
    });
    video.value.srcObject = stream;
    video.value.onloadeddata = () => {
      video.value.play();
      resizeCanvas();
    };
  } catch (error) {
    console.error('Error accessing webcam:', error);
  }
};

const loadModel = async () => {
  const publishable_key = 'rf_YEEYSbkz0HVcso1qNYkXykwRyMe2';
  const toLoad = { model: 'yolo-qqp8p', version: 3 };
  try {
    model = await window.roboflow.auth({ publishable_key }).load(toLoad);
  } catch (error) {
    console.error('Error loading model:', error);
  }
};

const detectFrame = () => {
  if (!model) {
    requestAnimationFrame(detectFrame);
    return;
  }
  model
    .detect(video.value)
    .then((predictions) => {
      updateDetectedItems(predictions);
      renderPredictions(predictions);
      requestAnimationFrame(detectFrame);
    })
    .catch((e) => {
      console.error('Detection error:', e);
      requestAnimationFrame(detectFrame);
    });
};

const updateDetectedItems = (predictions) => {
  const now = Date.now();

  predictions.forEach((prediction) => {
    const className = prediction.class;

    if (detectedItems.has(className)) {
      detectedItems.get(className).lastSeen = now;
      detectedItems.get(className).confidence = Math.round(
        prediction.confidence * 100
      );
    } else {
      detectedItems.set(className, {
        confidence: Math.round(prediction.confidence * 100),
        lastSeen: now,
      });
    }
  });

  // Remove items not seen in the last 5 seconds
  detectedItems.forEach((value, key) => {
    if (now - value.lastSeen > 5000) {
      detectedItems.delete(key);
    }
  });
};

const renderPredictions = (predictions) => {
  if (!ctx) {
    ctx = canvas.value.getContext('2d');
  }
  ctx.clearRect(0, 0, canvas.value.width, canvas.value.height);

  predictions.forEach((prediction) => {
    const x = prediction.bbox.x;
    const y = prediction.bbox.y;
    const width = prediction.bbox.width;
    const height = prediction.bbox.height;

    const left = x - width / 2;
    const top = y - height / 2;

    ctx.strokeStyle = prediction.color || 'red';
    ctx.lineWidth = 2;
    ctx.strokeRect(left, top, width, height);

    ctx.fillStyle = '#fff';
    ctx.fillText(
      `${prediction.class} - ${Math.round(prediction.confidence * 100)}%`,
      left,
      top + height + 10
    );
  });
};

const resizeCanvas = () => {
  if (video.value) {
    canvas.value.width = video.value.videoWidth;
    canvas.value.height = video.value.videoHeight;
    canvas.value.style.position = 'absolute';
    canvas.value.style.top = '0';
    canvas.value.style.left = '0';
    ctx = canvas.value.getContext('2d');
  }
};
</script>
