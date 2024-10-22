<template>
  <div
    class="h-screen bg-gradient-to-r from-[#4dbed2] to-indigo-500 px-8 py-6 font-sans"
  >
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <h1 class="text-4xl font-extrabold text-white mb-8">Object Detection</h1>

      <!-- Main Content -->
      <div class="relative flex flex-col lg:flex-row gap-8 items-start">
        <!-- Image Upload Container -->
        <div class="relative flex-1">
          <div
            class="relative rounded-2xl overflow-hidden shadow-2xl border-4 border-white/20"
          >
            <!-- File Input and Preview -->
            <div class="bg-white/10 backdrop-blur-lg p-6">
              <input
                type="file"
                @change="onFileChange"
                accept="image/*"
                class="mb-4"
              />
              <button
                @click="uploadFile"
                class="px-8 py-4 bg-[#626AEF] text-white font-semibold rounded-lg shadow-lg backdrop-blur-lg hover:bg-[#303AEB] transition duration-300"
              >
                Upload and Scan
              </button>
            </div>

            <!-- Image Preview Container -->
            <div v-if="state.uploadedImageUrl" class="relative">
              <img
                :src="state.uploadedImageUrl"
                alt="Uploaded"
                ref="uploadedImage"
                crossorigin="anonymous"
                @load="processImage"
                class="w-full"
              />
              <canvas ref="canvas" class="absolute top-0 left-0"></canvas>
            </div>
          </div>
        </div>

        <!-- Detection Results -->
        <div
          class="w-full lg:min-w-[400px] lg:w-auto bg-white/10 backdrop-blur-lg rounded-2xl p-6 shadow-xl"
        >
          <h2 class="text-2xl font-bold text-white mb-4">Detected Objects</h2>
          <div class="space-y-3">
            <div
              v-for="(item, index) in detectedItemsArray"
              :key="index"
              class="bg-white/20 backdrop-blur rounded-lg p-4 border border-white/30"
            >
              <div class="flex items-center justify-between gap-2 min-w-0">
                <!-- Left side with color indicator and name -->
                <div class="flex items-center gap-2 min-w-0 flex-1">
                  <div
                    class="flex-shrink-0 w-4 h-4 rounded-full"
                    :style="{ backgroundColor: item.color }"
                  ></div>
                  <div class="truncate">
                    <span class="text-lg font-semibold text-white">
                      {{ item.name }}
                      <span v-if="item.count > 1" class="text-sm">
                        (x{{ item.count }})
                      </span>
                    </span>
                  </div>
                </div>

                <!-- Confidence badge -->
                <span
                  class="flex-shrink-0 px-3 py-1 rounded-full text-sm font-medium whitespace-nowrap"
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
import { ref, reactive, computed } from "vue";
import axios from "axios";

// Add script for Roboflow
useHead({
  script: [
    {
      src: "https://cdn.roboflow.com/0.2.26/roboflow.js",
      async: true,
    },
  ],
});

const state = reactive({
  uploadedImageUrl: "",
  selectedFile: null,
});

const uploadedImage = ref(null);
const canvas = ref(null);
const detectedItems = reactive(new Map());
let model = null;

// Computed property for detected items
const detectedItemsArray = computed(() =>
  Array.from(detectedItems.entries()).map(([key, value]) => ({
    name: key,
    confidence: value.confidence,
    color: value.color,
    count: value.count,
  }))
);

onMounted(() => {
  const checkRoboflow = setInterval(() => {
    if (window.roboflow) {
      clearInterval(checkRoboflow);
      loadModel();
    }
  }, 100);
});

const loadModel = async () => {
  const publishable_key = "rf_YEEYSbkz0HVcso1qNYkXykwRyMe2";
  const toLoad = { model: "yolo-qqp8p", version: 3 };
  try {
    model = await window.roboflow.auth({ publishable_key }).load(toLoad);
    console.log("Model loaded successfully");
  } catch (error) {
    console.error("Error loading model:", error);
  }
};

const onFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    state.selectedFile = file;
  }
};

const uploadFile = async () => {
  if (!state.selectedFile) {
    alert("Please select a file first.");
    return;
  }

  const formData = new FormData();
  formData.append("file", state.selectedFile);
  formData.append("upload_preset", "uq8ofr4m");

  try {
    const response = await axios.post(
      "https://api.cloudinary.com/v1_1/dxxecptym/image/upload",
      formData
    );
    state.uploadedImageUrl = response.data.secure_url;
  } catch (error) {
    console.error("Error uploading file:", error);
    alert("Failed to upload file. Please try again.");
  }
};

const processImage = async () => {
  if (!model || !uploadedImage.value) return;

  const ctx = canvas.value.getContext("2d");
  canvas.value.width = uploadedImage.value.width;
  canvas.value.height = uploadedImage.value.height;

  try {
    const predictions = await model.detect(uploadedImage.value);
    updateDetectedItems(predictions);
    renderPredictions(predictions);
  } catch (error) {
    console.error("Error detecting objects:", error);
  }
};

const updateDetectedItems = (predictions) => {
  const countMap = new Map();
  detectedItems.clear();

  // First count occurrences
  predictions.forEach((prediction) => {
    const count = countMap.get(prediction.class) || 0;
    countMap.set(prediction.class, count + 1);
  });

  // Then update detectedItems
  predictions.forEach((prediction) => {
    const className = prediction.class;
    if (!detectedItems.has(className)) {
      detectedItems.set(className, {
        confidence: Math.round(prediction.confidence * 100),
        color: prediction.color || "#DD0F82",
        count: countMap.get(className),
        lastSeen: Date.now(),
      });
    }
  });
};

const renderPredictions = (predictions) => {
  const ctx = canvas.value.getContext("2d");
  ctx.clearRect(0, 0, canvas.value.width, canvas.value.height);

  predictions.forEach((prediction) => {
    const { bbox, color } = prediction;
    const x = bbox.x - bbox.width / 2;
    const y = bbox.y - bbox.height / 2;

    ctx.strokeStyle = color || "#DD0F82";
    ctx.lineWidth = 3;
    ctx.strokeRect(x, y, bbox.width, bbox.height);
  });
};

const getConfidenceClass = (confidence) => {
  if (confidence >= 80) return "bg-green-500 text-white";
  if (confidence >= 70) return "bg-yellow-500 text-white";
  return "bg-red-500 text-white";
};
</script>

<style scoped>
.backdrop-blur-lg {
  backdrop-filter: blur(12px);
}

/* Make the detection panel scrollable vertically if needed */
@media (min-height: 768px) {
  .space-y-3 {
    max-height: calc(100vh - 200px);
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: rgba(255, 255, 255, 0.3) transparent;
  }
}

/* Remove any width constraints from the panel */
@media (min-width: 1024px) {
  .lg\:min-w-\[400px\] {
    min-width: 400px;
    width: auto;
  }
}
</style>
