<template>
        <div class="container h-[calc(100vh-64px)] bg-gradient-to-r from-[#4dbed2] to-indigo-500 flex items-center px-8 overflow-hidden"
    >
    <h1>Object Detection with Webcam</h1>
    <video id="video" autoplay></video>
    <div id="detected-items"></div>
  </div>
</template>
 
<script>
export default {
  name: 'Scan',
  mounted() {
    // This lifecycle hook will be used for future implementations
    // Here you can initialize the webcam access or any other logic
  },
};
</script>
 
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #f0f0f0;
}
 
video {
  width: 640px;
  height: 480px;
  border: 2px solid #000;
}
 
#detected-items {
  margin-top: 20px;
  width: 640px;
  background: #fff;
  border: 1px solid #ccc;
  padding: 10px;
  max-height: 300px;
  overflow-y: auto;
}
</style>