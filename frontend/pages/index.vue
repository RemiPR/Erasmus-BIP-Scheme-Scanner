<template>
  <div>
    <!-- Main Content -->
    <div
      class="h-[calc(100vh-64px)] bg-gradient-to-r from-[#4dbed2] to-indigo-500 flex items-center px-8 overflow-hidden"
    >
      <!-- Content Wrapper -->
      <div
        class="relative grid grid-cols-1 lg:grid-cols-2 gap-16 w-full items-center"
      >
        <!-- Large Circle Shape positioned at the bottom-left corner -->
        <div
          class="absolute bottom-[-32rem] left-[18rem] w-[600px] h-[600px] lg:w-[600px] lg:h-[600px] bg-[#D963C5] rounded-full"
        ></div>

        <!-- Left Column: Text and Buttons with more margin -->
        <div class="relative text-left space-y-6 lg:pr-16 lg:ml-10">
          <div class="flex items-center">
            <h1 class="text-5xl lg:text-6xl font-extrabold text-white">
              Scheme Scanner
            </h1>
            <video autoplay loop muted playsinline>
              <!-- Path for a file in the static folder -->
              <source src="/animation.webm" type="video/webm" />
              <!-- Alternative text or fallback message -->
              Your browser does not support the video tag.
            </video>
          </div>
          <p class="text-xl text-gray-200 leading-loose">
            Scan and upload your PFD, P&ID schemes with ease.
            <span class="block"
              >Our tool is built to handle complex structures efficiently.</span
            >
          </p>
          <div class="flex space-x-4">
            <NuxtLink
              to="/scan"
              class="px-8 py-4 bg-[#DD0F82] text-white font-semibold rounded-lg shadow-lg backdrop-blur-lg hover:bg-pink-500 transition duration-300 transform hover:scale-105 focus:outline-none"
            >
              Scan
            </NuxtLink>
            <NuxtLink
              to="/upload"
              class="px-8 py-4 bg-[#626AEF] text-white font-semibold rounded-lg shadow-lg backdrop-blur-lg hover:bg-[#303AEB] hover:border-white transition duration-300 transform hover:scale-105 focus:outline-none"
            >
              Upload a file
            </NuxtLink>
          </div>
        </div>

        <!-- Right Column: Blob and SVG Illustration -->
        <div class="relative w-full flex justify-center items-center">
          <!-- Blob Shape -->
          <div
            class="blob w-[400px] h-[400px] lg:w-[550px] lg:h-[550px] bg-gradient-to-tr from-purple-400 via-pink-500 to-red-400 overflow-hidden flex justify-center items-center"
            style="position: relative; right: -20px"
          >
            <!-- SVG Illustration inside Blob -->
            <div class="w-3/4 h-3/4">
              <LandingSvgAnimation />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Blob Shape with Left Edge Sticking Out More */
.blob {
  clip-path: polygon(
    45% 0%,
    90% 10%,
    100% 50%,
    85% 90%,
    50% 100%,
    20% 90%,
    0% 50%,
    10% 15%
  );
  border-radius: 50% 40% 60% 45% / 35% 55% 65% 50%;
}
</style>
