<template>
  <div
    class="h-screen bg-gradient-to-r from-[#4dbed2] to-indigo-500 px-8 py-6 font-sans"
  >
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <h1 class="text-4xl font-extrabold text-white mb-8">Object Detection</h1>

      <!-- Main Content -->
      <div class="relative flex flex-col lg:flex-row gap-8 items-start">
        <!-- Video Container -->
        <div class="relative flex-1">
          <div
            class="relative rounded-2xl overflow-hidden shadow-2xl border-4 border-white/20"
          >
            <video
              ref="video"
              autoplay
              muted
              playsinline
              class="w-full h-full"
            ></video>
            <canvas ref="canvas" class="absolute top-0 left-0"></canvas>
          </div>
        </div>

        <!-- Detection Results -->
        <div
          class="w-full lg:w-[400px] bg-white/10 backdrop-blur-lg rounded-2xl p-6 shadow-xl"
        >
          <h2 class="text-2xl font-bold text-white mb-4">Detected Objects</h2>
          <div class="space-y-3">
            <div
              v-for="(item, index) in detectedItemsArray"
              :key="index"
              class="bg-white/20 backdrop-blur rounded-lg p-4 border border-white/30"
            >
              <div class="flex justify-between items-center">
                <span class="text-lg font-semibold text-white">{{
                  item.name
                }}</span>
                <span
                  class="px-3 py-1 rounded-full text-sm font-medium"
                  :class="getConfidenceClass(item.confidence)"
                >
                  {{ item.confidence }}%
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
useHead({
  script: [
    {
      src: "https://cdn.roboflow.com/0.2.26/roboflow.js",
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
  window.removeEventListener("resize", resizeCanvas);
});

const initializeApp = async () => {
  await startVideoStream();
  await loadModel();
  detectFrame();
  window.addEventListener("resize", resizeCanvas);
};

const startVideoStream = async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: false,
      video: {
        facingMode: "environment",
      },
    });
    video.value.srcObject = stream;
    video.value.onloadeddata = () => {
      video.value.play();
      resizeCanvas();
    };
  } catch (error) {
    console.error("Error accessing webcam:", error);
  }
};

const loadModel = async () => {
  const publishable_key = "rf_YEEYSbkz0HVcso1qNYkXykwRyMe2";
  const toLoad = { model: "yolo-qqp8p", version: 3 };
  try {
    model = await window.roboflow.auth({ publishable_key }).load(toLoad);
  } catch (error) {
    console.error("Error loading model:", error);
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
      console.error("Detection error:", e);
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
    ctx = canvas.value.getContext("2d");
  }
  ctx.clearRect(0, 0, canvas.value.width, canvas.value.height);

  predictions.forEach((prediction) => {
    const x = prediction.bbox.x;
    const y = prediction.bbox.y;
    const width = prediction.bbox.width;
    const height = prediction.bbox.height;

    const left = x - width / 2;
    const top = y - height / 2;

    // Draw box
    ctx.strokeStyle = prediction.color || "#DD0F82";
    ctx.lineWidth = 3;
    ctx.strokeRect(left, top, width, height);

    // Draw label background
    const label = `${prediction.class} - ${Math.round(
      prediction.confidence * 100
    )}%`;
    ctx.font = "bold 16px Inter, sans-serif";
    const textMetrics = ctx.measureText(label);
    const padding = 5;

    ctx.fillStyle = "rgba(0, 0, 0, 0.7)";
    ctx.fillRect(left, top - 30, textMetrics.width + padding * 2, 24);

    // Draw label text
    ctx.fillStyle = "#ffffff";
    ctx.fillText(label, left + padding, top - 12);
  });
};
// Add this new function for confidence score styling
const getConfidenceClass = (confidence) => {
  if (confidence >= 90) {
    return "bg-green-500 text-white";
  } else if (confidence >= 70) {
    return "bg-yellow-500 text-white";
  } else {
    return "bg-red-500 text-white";
  }
};

const resizeCanvas = () => {
  if (video.value) {
    canvas.value.width = video.value.videoWidth;
    canvas.value.height = video.value.videoHeight;
    canvas.value.style.position = "absolute";
    canvas.value.style.top = "0";
    canvas.value.style.left = "0";
    ctx = canvas.value.getContext("2d");
  }
};
</script>

<style>
/* Add any additional styles here */
.backdrop-blur-lg {
  backdrop-filter: blur(12px);
}
</style>
