<template>
  <div>
    <!-- Navigation Bar -->
    <nav
      class="bg-gradient-to-r from-[#e4067e] to-[#4dbed2] text-white py-4 px-8"
    >
      <div class="flex justify-between items-center mx-auto">
        <!-- Logo and Navigation Links -->
        <div class="flex items-center space-x-8">
          <!-- Logo Image -->
          <NuxtLink to="/" class="flex items-center space-x-4">
            <img src="/logo.svg" alt="logo" class="h-8 w-auto" />
          </NuxtLink>

          <!-- Navigation Links -->
          <div class="flex space-x-8 font-semibold text-lg">
            <div class="flex items-center space-x-1 group">
              <a href="#" class="hover:text-gray-200">Study Info</a>
              <Icon
                name="mdi:chevron-down"
                class="w-5 h-5 text-white transition-transform duration-300 transform group-hover:-rotate-180"
              />
            </div>
            <div class="flex items-center space-x-1 group">
              <a href="#" class="hover:text-gray-200">Student Life</a>
              <Icon
                name="mdi:chevron-down"
                class="w-5 h-5 text-white transition-transform duration-300 transform group-hover:-rotate-180"
              />
            </div>
            <div class="flex items-center space-x-1 group">
              <a href="#" class="hover:text-gray-200">Services</a>
              <Icon
                name="mdi:chevron-down"
                class="w-5 h-5 text-white transition-transform duration-300 transform group-hover:-rotate-180"
              />
            </div>
          </div>
        </div>

        <!-- User Info -->
        <div class="flex items-center space-x-4">
          <!-- User Name and Study Group, and Vertical Line with Text Aligned -->
          <div class="flex items-center space-x-4">
            <!-- Vertical Line and Two-line Text aligned with User Info -->
            <div class="flex items-center space-x-2">
              <div class="border-l-2 border-white h-8"></div>
              <div
                class="text-xs font-bold leading-none flex flex-col justify-center"
              >
                <span class="block">TALLINNA</span>
                <span class="block">TEHNIKAÜLIKOOL</span>
              </div>
            </div>
            <!-- Student Name and Group Info -->
            <div class="text-right text-[#342B60] flex flex-col justify-center">
              <span class="block text-sm font-semibold leading-none"
                >Student Name</span
              >
              <span class="block text-xs leading-tight"
                >Study group: Blue team</span
              >
            </div>
          </div>

          <!-- Avatar Icon -->
          <div class="text-white w-8 h-8 flex items-center justify-center">
            <Icon class="h-full w-full" name="tdesign:user-avatar" />
          </div>
        </div>
      </div>
    </nav>
    <slot />
  </div>
</template>
