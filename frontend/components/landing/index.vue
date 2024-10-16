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
          <div class="flex items-center space-x-4">
            <img src="/logo.svg" alt="logo" class="h-8 w-auto" />
          </div>

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

    <!-- Main Content -->
    <div
      class="h-[calc(100vh-64px)] bg-gradient-to-r from-[#4dbed2] to-indigo-500 flex items-center px-8"
    >
      <!-- Content Wrapper -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 w-full items-center">
        <!-- Left Column: Text and Buttons with more margin -->
        <div class="text-left space-y-6 lg:pr-16 lg:ml-10">
          <h1 class="text-5xl lg:text-6xl font-extrabold text-white">
            Scheme Scanner
          </h1>
          <p class="text-lg text-gray-200">
            Scan and upload your PFD, P&ID schemes with ease. Our tool is built
            to handle complex structures efficiently.
          </p>
          <div class="flex space-x-4">
            <button
              class="px-8 py-4 bg-white/20 text-white font-semibold rounded-lg shadow-lg backdrop-blur-lg hover:bg-white/30 transition duration-300 transform hover:scale-105 focus:outline-none"
            >
              Scan
            </button>
            <button
              class="px-8 py-4 bg-white/20 text-white font-semibold rounded-lg shadow-lg border-2 border-white/30 backdrop-blur-lg hover:bg-white/30 hover:border-white transition duration-300 transform hover:scale-105 focus:outline-none"
            >
              Upload a file
            </button>
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
              <svg
                class="animated"
                id="freepik_stories-files-sent"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 500 500"
                version="1.1"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                xmlns:svgjs="http://svgjs.com/svgjs"
              >
                <g
                  id="freepik--background-complete--inject-68"
                  class="animable"
                  style="transform-origin: 250px 228.23px"
                >
                  <path
                    d="M237,337.8H43.91a5.71,5.71,0,0,1-5.7-5.71V60.66A5.71,5.71,0,0,1,43.91,55H237a5.71,5.71,0,0,1,5.71,5.71V332.09A5.71,5.71,0,0,1,237,337.8ZM43.91,55.2a5.46,5.46,0,0,0-5.45,5.46V332.09a5.46,5.46,0,0,0,5.45,5.46H237a5.47,5.47,0,0,0,5.46-5.46V60.66A5.47,5.47,0,0,0,237,55.2Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 140.46px 196.4px;
                    "
                    id="elqry4of1r34m"
                    class="animable"
                  ></path>
                  <path
                    d="M453.31,337.8H260.21a5.72,5.72,0,0,1-5.71-5.71V60.66A5.72,5.72,0,0,1,260.21,55h193.1A5.71,5.71,0,0,1,459,60.66V332.09A5.71,5.71,0,0,1,453.31,337.8ZM260.21,55.2a5.47,5.47,0,0,0-5.46,5.46V332.09a5.47,5.47,0,0,0,5.46,5.46h193.1a5.47,5.47,0,0,0,5.46-5.46V60.66a5.47,5.47,0,0,0-5.46-5.46Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 356.75px 196.4px;
                    "
                    id="eltz79e3inlp"
                    class="animable"
                  ></path>
                  <rect
                    x="416.78"
                    y="398.49"
                    width="33.12"
                    height="0.25"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 433.34px 398.615px;
                    "
                    id="eleoab7oyy4pq"
                    class="animable"
                  ></rect>
                  <rect
                    x="322.53"
                    y="401.21"
                    width="8.69"
                    height="0.25"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 326.875px 401.335px;
                    "
                    id="el5fzztj1gy2a"
                    class="animable"
                  ></rect>
                  <rect
                    x="396.59"
                    y="389.21"
                    width="19.19"
                    height="0.25"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 406.185px 389.335px;
                    "
                    id="elc8adlmhj11g"
                    class="animable"
                  ></rect>
                  <rect
                    x="52.46"
                    y="390.89"
                    width="43.19"
                    height="0.25"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 74.055px 391.015px;
                    "
                    id="ellmdmrdu9ln8"
                    class="animable"
                  ></rect>
                  <rect
                    x="104.56"
                    y="390.89"
                    width="6.33"
                    height="0.25"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 107.725px 391.015px;
                    "
                    id="el2vy1wudxzlp"
                    class="animable"
                  ></rect>
                  <rect
                    x="131.47"
                    y="395.11"
                    width="93.68"
                    height="0.25"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 178.31px 395.235px;
                    "
                    id="elyjcrqoqssu"
                    class="animable"
                  ></rect>
                  <rect
                    y="382.4"
                    width="500"
                    height="0.25"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 250px 382.525px;
                    "
                    id="elxx7bhaan98"
                    class="animable"
                  ></rect>
                  <rect
                    x="37.32"
                    y="95.16"
                    width="117.62"
                    height="173.8"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 96.13px 182.06px;
                    "
                    id="el3q043m0uecl"
                    class="animable"
                  ></rect>
                  <rect
                    x="41.65"
                    y="95.16"
                    width="117.62"
                    height="173.8"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 100.46px 182.06px;
                    "
                    id="elsm63niidu2d"
                    class="animable"
                  ></rect>
                  <rect
                    x="47.37"
                    y="187.04"
                    width="105.95"
                    height="71.74"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 100.345px 222.91px;
                    "
                    id="ell5pph3jeb"
                    class="animable"
                  ></rect>
                  <rect
                    x="47.37"
                    y="102.22"
                    width="105.95"
                    height="84.82"
                    style="
                      fill: rgb(255, 255, 255);
                      transform-origin: 100.345px 144.63px;
                    "
                    id="elvmfvn1h57m"
                    class="animable"
                  ></rect>
                  <rect
                    x="149.59"
                    y="102.22"
                    width="3.73"
                    height="156.56"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 151.455px 180.5px;
                    "
                    id="eledmd18taqni"
                    class="animable"
                  ></rect>
                  <g id="ellbnk468241o">
                    <rect
                      x="96.62"
                      y="137.46"
                      width="3.78"
                      height="102.95"
                      style="
                        fill: rgb(224, 224, 224);
                        transform-origin: 98.51px 188.935px;
                        transform: rotate(-90deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <rect
                    x="45.37"
                    y="180.69"
                    width="107.95"
                    height="6.35"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 99.345px 183.865px;
                    "
                    id="el0vol3sr97sj"
                    class="animable"
                  ></rect>
                  <rect
                    x="275.14"
                    y="301.53"
                    width="182.7"
                    height="82.01"
                    rx="19.67"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 366.49px 342.535px;
                    "
                    id="el4xb1ii70z6n"
                    class="animable"
                  ></rect>
                  <rect
                    x="265.51"
                    y="302.13"
                    width="182.7"
                    height="82.01"
                    rx="19.67"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 356.86px 343.135px;
                    "
                    id="elz2ju2tv9hgf"
                    class="animable"
                  ></rect>
                  <path
                    d="M288.7,309.87H426.1a13.74,13.74,0,0,1,13.74,13.74v16.86a0,0,0,0,1,0,0H275a0,0,0,0,1,0,0V323.6A13.74,13.74,0,0,1,288.7,309.87Z"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 357.42px 325.17px;
                    "
                    id="eld1ggq2xrjpa"
                    class="animable"
                  ></path>
                  <path
                    d="M275,344.6H439.84a0,0,0,0,1,0,0v16.86A13.74,13.74,0,0,1,426.1,375.2H288.7A13.74,13.74,0,0,1,275,361.46V344.6A0,0,0,0,1,275,344.6Z"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 357.42px 359.9px;
                    "
                    id="el2gtk68in3hu"
                    class="animable"
                  ></path>
                  <rect
                    x="365.3"
                    y="315.79"
                    width="30.19"
                    height="24.87"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 380.395px 328.225px;
                    "
                    id="el3a2mv0krgtx"
                    class="animable"
                  ></rect>
                  <rect
                    x="357.57"
                    y="315.79"
                    width="7.73"
                    height="24.87"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 361.435px 328.225px;
                    "
                    id="el5pf6i8wwofg"
                    class="animable"
                  ></rect>
                  <path
                    d="M364,334a2.54,2.54,0,1,1-2.54-2.54A2.54,2.54,0,0,1,364,334Z"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 361.46px 334px;
                    "
                    id="elc680uf8v6e7"
                    class="animable"
                  ></path>
                  <rect
                    x="380.73"
                    y="311.95"
                    width="22.68"
                    height="28.71"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 392.07px 326.305px;
                    "
                    id="ela7vxe5ud6qo"
                    class="animable"
                  ></rect>
                  <rect
                    x="374.18"
                    y="311.95"
                    width="6.56"
                    height="28.71"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 377.46px 326.305px;
                    "
                    id="elm1qw57qsohs"
                    class="animable"
                  ></rect>
                  <circle
                    cx="377.46"
                    cy="316.12"
                    r="2.25"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 377.46px 316.12px;
                    "
                    id="elumygmul7hs"
                    class="animable"
                  ></circle>
                  <circle
                    cx="377.46"
                    cy="316.12"
                    r="2.25"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 377.46px 316.12px;
                    "
                    id="elvjq31srijyk"
                    class="animable"
                  ></circle>
                  <rect
                    x="387.41"
                    y="315.79"
                    width="19.12"
                    height="24.87"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 396.97px 328.225px;
                    "
                    id="eltghjxd63d0m"
                    class="animable"
                  ></rect>
                  <rect
                    x="383.04"
                    y="315.79"
                    width="4.37"
                    height="24.87"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 385.225px 328.225px;
                    "
                    id="el9s5amucllyp"
                    class="animable"
                  ></rect>
                  <rect
                    x="403.06"
                    y="320"
                    width="25.08"
                    height="20.67"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 415.6px 330.335px;
                    "
                    id="elecgh3zchqt5"
                    class="animable"
                  ></rect>
                  <rect
                    x="396.64"
                    y="320"
                    width="6.42"
                    height="20.67"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 399.85px 330.335px;
                    "
                    id="elpfqao12scz"
                    class="animable"
                  ></rect>
                  <rect
                    x="415.87"
                    y="316.81"
                    width="18.84"
                    height="23.85"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 425.29px 328.735px;
                    "
                    id="el0do4y13mdsec"
                    class="animable"
                  ></rect>
                  <rect
                    x="410.44"
                    y="316.81"
                    width="5.45"
                    height="23.85"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 413.165px 328.735px;
                    "
                    id="eluedlrpdsgks"
                    class="animable"
                  ></rect>
                  <rect
                    x="421.43"
                    y="320"
                    width="18.3"
                    height="20.67"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 430.58px 330.335px;
                    "
                    id="eljv5a0obbb2"
                    class="animable"
                  ></rect>
                  <rect
                    x="417.79"
                    y="320"
                    width="3.63"
                    height="20.67"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 419.605px 330.335px;
                    "
                    id="eli8c1v4c6mqe"
                    class="animable"
                  ></rect>
                  <rect
                    x="299.96"
                    y="349.38"
                    width="23.37"
                    height="24.87"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 311.645px 361.815px;
                    "
                    id="eltj43gpblh6b"
                    class="animable"
                  ></rect>
                  <rect
                    x="293.98"
                    y="349.38"
                    width="5.99"
                    height="24.87"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 296.975px 361.815px;
                    "
                    id="elihgup5fh8t"
                    class="animable"
                  ></rect>
                  <rect
                    x="311.9"
                    y="345.54"
                    width="17.55"
                    height="28.71"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 320.675px 359.895px;
                    "
                    id="elx4dvos501g"
                    class="animable"
                  ></rect>
                  <rect
                    x="306.84"
                    y="345.54"
                    width="5.07"
                    height="28.71"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 309.375px 359.895px;
                    "
                    id="elvdjm8c44xmp"
                    class="animable"
                  ></rect>
                  <rect
                    x="379.68"
                    y="349.38"
                    width="23.37"
                    height="24.87"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 391.365px 361.815px;
                    "
                    id="el4g7lf2lr1g5"
                    class="animable"
                  ></rect>
                  <rect
                    x="373.7"
                    y="349.38"
                    width="5.99"
                    height="24.87"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 376.695px 361.815px;
                    "
                    id="elfacedzi8h8f"
                    class="animable"
                  ></rect>
                  <rect
                    x="391.62"
                    y="345.54"
                    width="17.55"
                    height="28.71"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 400.395px 359.895px;
                    "
                    id="eln0nbmd1v0gr"
                    class="animable"
                  ></rect>
                  <rect
                    x="386.56"
                    y="345.54"
                    width="5.08"
                    height="28.71"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 389.1px 359.895px;
                    "
                    id="eluzvjbmf14un"
                    class="animable"
                  ></rect>
                  <rect
                    x="317.08"
                    y="349.38"
                    width="14.8"
                    height="24.87"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 324.48px 361.815px;
                    "
                    id="el2qos525o5ob"
                    class="animable"
                  ></rect>
                  <rect
                    x="313.7"
                    y="349.38"
                    width="3.38"
                    height="24.87"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 315.39px 361.815px;
                    "
                    id="eltmqjpbsc5k9"
                    class="animable"
                  ></rect>
                  <rect
                    x="329.19"
                    y="353.59"
                    width="19.41"
                    height="20.67"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 338.895px 363.925px;
                    "
                    id="eln11vix6bzc"
                    class="animable"
                  ></rect>
                  <rect
                    x="324.22"
                    y="353.59"
                    width="4.97"
                    height="20.67"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 326.705px 363.925px;
                    "
                    id="elzqxp29eryli"
                    class="animable"
                  ></rect>
                  <rect
                    x="339.11"
                    y="350.4"
                    width="14.58"
                    height="23.85"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 346.4px 362.325px;
                    "
                    id="eloa99wysg8m"
                    class="animable"
                  ></rect>
                  <rect
                    x="334.9"
                    y="350.4"
                    width="4.22"
                    height="23.85"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 337.01px 362.325px;
                    "
                    id="el19j60yn3t3z"
                    class="animable"
                  ></rect>
                  <rect
                    x="343.41"
                    y="353.59"
                    width="14.17"
                    height="20.67"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 350.495px 363.925px;
                    "
                    id="el5kcq5yf5quy"
                    class="animable"
                  ></rect>
                  <rect
                    x="340.59"
                    y="353.59"
                    width="2.81"
                    height="20.67"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 341.995px 363.925px;
                    "
                    id="elc9vz7q08a1j"
                    class="animable"
                  ></rect>
                  <path
                    d="M340.45,277.68a2.52,2.52,0,0,0-2.67-1.33,2.64,2.64,0,0,0-2,2.31,2.21,2.21,0,0,0-2.53-.07,2.51,2.51,0,0,0-1,2.45,1.87,1.87,0,0,0-2.71.55,2.1,2.1,0,0,0,.83,2.78,1.34,1.34,0,0,0,.07,2.66,1.45,1.45,0,0,0-1.33,1.28,1.49,1.49,0,0,0,1,1.57,1.22,1.22,0,0,0-.29,1.88,1.1,1.1,0,0,0,1.73-.55.35.35,0,0,0,.56.09.41.41,0,0,0-.1-.6.66.66,0,0,0,1.14-.29,1.65,1.65,0,0,0,2.23,1.76,1,1,0,0,0,.66,1.36,2.33,2.33,0,0,0,1.61-.32,3.54,3.54,0,0,1,1.58-.53,5.11,5.11,0,0,1,1.41.39,4.25,4.25,0,0,0,4.31-1.14,1.84,1.84,0,0,0,3.07-.46,1.3,1.3,0,0,0,2.53.15l0,.78a1.63,1.63,0,0,0,1.67-2.18,1.67,1.67,0,0,0,1.59-1.45,1.72,1.72,0,0,0-1.18-1.83,3.24,3.24,0,0,0,.06-6.14,1.53,1.53,0,0,0-1.47.21.92.92,0,0,0,0,1.39,3,3,0,0,0-1.26-3.34,2.65,2.65,0,0,0-3.34.72,1.66,1.66,0,0,0,0-1.85,1.45,1.45,0,0,0-1.66-.55,1.67,1.67,0,0,0-1.8-1.37,1.75,1.75,0,0,0-1.36,1.86.84.84,0,0,0-1.53-.29C339.86,277.45,340.45,277.68,340.45,277.68Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 341.983px 284.782px;
                    "
                    id="eluj5c6stvd5d"
                    class="animable"
                  ></path>
                  <path
                    d="M340.75,285.67a1.53,1.53,0,0,0-1.15-.28,1.07,1.07,0,0,0-.83.78.81.81,0,0,0,.56.94c.47.12.95-.28,1.43-.21.18,0,.34.11.51.15a2.44,2.44,0,0,0,2-.7,2,2,0,0,0,.55-.52.7.7,0,0,0,.06-.72.93.93,0,0,0-.95-.31,3.73,3.73,0,0,0-1.94.81l.05-.33Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 341.353px 285.952px;
                    "
                    id="elssh8wij913"
                    class="animable"
                  ></path>
                  <path
                    d="M350.88,285.07a1.63,1.63,0,0,0-.61-.32.61.61,0,0,0-.63.17.64.64,0,0,0,.18.84,1.78,1.78,0,0,0,.88.3c.33.05.73.06.89-.22a.55.55,0,0,0-.15-.64,1.62,1.62,0,0,0-.63-.31Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 350.595px 285.405px;
                    "
                    id="elexkhvoj60ch"
                    class="animable"
                  ></path>
                  <path
                    d="M334.87,279.8a2.22,2.22,0,0,0-1.29,1.55.51.51,0,0,0,.14.57.56.56,0,0,0,.44,0l1.85-.44a2.57,2.57,0,0,0-.83.45.88.88,0,0,0-.32.84.86.86,0,0,0,.86.58,1.79,1.79,0,0,0,1-.41,1.32,1.32,0,0,0,.65-.95c0-.39-.5-.76-.8-.51a7,7,0,0,0,2-.9,2,2,0,0,0,.57-.54.77.77,0,0,0,.06-.76c-.63-1.15-1.43.54-1.82.69C336.65,280.26,335.81,279.4,334.87,279.8Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 336.409px 281.116px;
                    "
                    id="elzll403rn26j"
                    class="animable"
                  ></path>
                  <path
                    d="M332,284.71a.62.62,0,0,0,.16.65.4.4,0,0,0,.59-.12,2,2,0,0,0-1.11.62.73.73,0,0,0,.22,1.1,1,1,0,0,0,.77-.18,13.41,13.41,0,0,0,1.91-1.26c-.18.43.26.91.72,1a2.19,2.19,0,0,0,1.29-.45c.49-.3,1-.75.92-1.3a1,1,0,0,0-1.2-.56,2.91,2.91,0,0,0-1.17.89c.26-.37-.1-.94-.56-1a1.37,1.37,0,0,0-1.16.54c.52-.29.63-1-.06-1.11C332.86,283.42,332.1,284.34,332,284.71Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 334.478px 285.248px;
                    "
                    id="el0eyz799ypwh"
                    class="animable"
                  ></path>
                  <path
                    d="M346.15,283.06a.79.79,0,0,0-1,.51.78.78,0,0,0,.61.92,1.18,1.18,0,0,0-.78.41.64.64,0,0,0-.17.47.56.56,0,0,0,.55.42,1.7,1.7,0,0,0,.73-.2,1.31,1.31,0,0,0-.71.2.46.46,0,0,0-.11.66.61.61,0,0,0,.59.06,2.83,2.83,0,0,0,1.22-.68,1.2,1.2,0,0,0,1,.43.7.7,0,0,0,.58-.83.75.75,0,0,0-.63-.46,2.07,2.07,0,0,0-.81.12,1.49,1.49,0,0,0,.65-.71c.1-.31-.11-.73-.44-.7s-.55.52-.84.7C346.26,284.05,346.93,283.35,346.15,283.06Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 346.741px 284.79px;
                    "
                    id="ell22szjd9iyr"
                    class="animable"
                  ></path>
                  <path
                    d="M339.54,281.53a1.49,1.49,0,0,0-.54,1.34,1.59,1.59,0,0,0,.8,1.38,1.27,1.27,0,0,0,1.63-1,1.79,1.79,0,0,0-1-1.79A1,1,0,0,0,339.54,281.53Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 340.214px 282.847px;
                    "
                    id="elw0y66u80th"
                    class="animable"
                  ></path>
                  <path
                    d="M344.22,280.93l.17.15a.84.84,0,1,0-1.23,1.13.88.88,0,0,0,1.23-.09,1.24,1.24,0,0,0,1.46-.27,1,1,0,0,0-.2-1.39.78.78,0,0,0-1.12.66l-.2-.22Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 344.46px 281.4px;
                    "
                    id="elv0qiaqukcl"
                    class="animable"
                  ></path>
                  <path
                    d="M349.39,281.77a2.61,2.61,0,0,0-.8,1.12.93.93,0,0,0,.53,1.14c.45.11.87-.26,1.13-.64a1.42,1.42,0,0,0,.27-1.18c-.13-.4-.7-.63-1-.33Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 349.55px 282.896px;
                    "
                    id="elj8x7t3t5ci"
                    class="animable"
                  ></path>
                  <path
                    d="M341.94,279.06a.76.76,0,0,0-1.05-.3.92.92,0,0,0-.33,1.1,1.17,1.17,0,0,0,1,.69c.5.05,1.1-.36,1-.86a1.07,1.07,0,0,0,1,.37,2.64,2.64,0,0,0,1-.38c.43-.25.88-.62.84-1.11a.87.87,0,0,0-.81-.73,1.45,1.45,0,0,0-1.07.4c-.23.2-.43.44-.68.62a.84.84,0,0,1-.87.12Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 342.948px 279.196px;
                    "
                    id="el3qb1s58qw8s"
                    class="animable"
                  ></path>
                  <polygon
                    points="348.3 301.8 335.49 301.8 334.24 288.89 349.55 288.89 348.3 301.8"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 341.895px 295.345px;
                    "
                    id="elvtvs99718yr"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="350.55 289.56 333.12 289.56 332.81 287.84 350.86 287.84 350.55 289.56"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 341.835px 288.7px;
                    "
                    id="elqr3in4w0i28"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="335 340.63 320.3 340.63 324.91 325.79 325.58 323.63 328.91 323.63 335 340.63"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 327.65px 332.13px;
                    "
                    id="elhdk589calwh"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="325.58 323.63 324.91 325.79 320.3 340.63 306.71 340.43 302.34 325.79 301.67 323.63 325.58 323.63"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 313.625px 332.13px;
                    "
                    id="el3m1zoe187br"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="325.58 323.63 324.91 325.79 320.3 340.63 292.39 340.22 298.34 323.63 325.58 323.63"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 308.985px 332.13px;
                    "
                    id="el07cim8ucw4rd"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="325.58 323.63 324.91 325.79 297.57 325.79 298.34 323.63 325.58 323.63"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 311.575px 324.71px;
                    "
                    id="elcfs56owf81t"
                    class="animable"
                  ></polygon>
                  <path
                    d="M301.77,332.84h-6.13l2.14-6,5.86.06Zm-5.42-.5h5l1.56-5-4.83-.05Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 299.64px 329.84px;
                    "
                    id="ely2b79mu7zx"
                    class="animable"
                  ></path>
                  <path
                    d="M308.63,332.84H302.5l2.13-6,5.87.06Zm-5.43-.5h5.06l1.56-5-4.83-.05Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 306.5px 329.84px;
                    "
                    id="eljo66s4j3sqs"
                    class="animable"
                  ></path>
                  <path
                    d="M315.48,332.84h-6.13l2.14-6,5.86.06Zm-5.42-.5h5.06l1.55-5-4.83-.05Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 313.35px 329.84px;
                    "
                    id="el8stay9g3sst"
                    class="animable"
                  ></path>
                  <path
                    d="M322.34,332.84h-6.13l2.14-6,5.86.06Zm-5.42-.5H322l1.56-5-4.83-.05Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 320.21px 329.84px;
                    "
                    id="elmmawpfzjzie"
                    class="animable"
                  ></path>
                  <path
                    d="M299.63,339.25H293.5l2.14-6,5.86.07Zm-5.42-.5h5.05l1.56-5-4.83,0Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 297.5px 336.25px;
                    "
                    id="el4khxstd14sn"
                    class="animable"
                  ></path>
                  <path
                    d="M306.49,339.25h-6.13l2.14-6,5.86.07Zm-5.42-.5h5.05l1.56-5-4.83,0Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 304.36px 336.25px;
                    "
                    id="elk6sfzc6vtl"
                    class="animable"
                  ></path>
                  <path
                    d="M313.34,339.25h-6.13l2.14-6,5.86.07Zm-5.42-.5H313l1.56-5-4.84,0Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 311.21px 336.25px;
                    "
                    id="elszr5k7wrnpo"
                    class="animable"
                  ></path>
                  <path
                    d="M320.2,339.25h-6.13l2.14-6,5.86.07Zm-5.42-.5h5.05l1.56-5-4.83,0Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 318.07px 336.25px;
                    "
                    id="eljkkqgg7rlxm"
                    class="animable"
                  ></path>
                  <path
                    d="M413.21,293.79c0,3.15.5,5.19,1.33,6.5a3.44,3.44,0,0,0,2.92,1.53H422a3.43,3.43,0,0,0,2.91-1.53c.84-1.31,1.33-3.35,1.33-6.5,0-4.57-2-8.23-2.64-11.15-.24-1.05.54-4.28.54-4.28h-8.85s.78,3.23.54,4.28C415.2,285.56,413.21,289.22,413.21,293.79Z"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 419.725px 290.09px;
                    "
                    id="el14irw3jeq01"
                    class="animable"
                  ></path>
                  <path
                    d="M422.69,256.3a4.7,4.7,0,0,0-2.36,1.53c-.87,1.16.63,3.88.63,3.88a3.68,3.68,0,0,0,3.18,1l1.77-.43S424,257,422.7,256.65Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 422.984px 259.53px;
                    "
                    id="elqlzwkw9j6yl"
                    class="animable"
                  ></path>
                  <path
                    d="M429.65,257.57c-.23,2.33-2.19,4.94-4.27,4.74s-3.47-3.17-3.24-5.49,1.93-2.24,4-2S429.89,255.25,429.65,257.57Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 425.894px 258.513px;
                    "
                    id="elh7bi8lxjvh"
                    class="animable"
                  ></path>
                  <path
                    d="M423.8,255.77s1.33,1.54,4.68,1.42C428.48,257.19,422.77,259.61,423.8,255.77Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 426.078px 256.856px;
                    "
                    id="el0ef8my5a7tru"
                    class="animable"
                  ></path>
                  <path
                    d="M425.26,255.58s1.86,0,1.75.78c0,0,1.54.2,1.45-.48S425.26,255.58,425.26,255.58Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 426.862px 255.931px;
                    "
                    id="eli6dobjrmyq"
                    class="animable"
                  ></path>
                  <path
                    d="M423.8,255.77s1.33,1.54,4.68,1.42C428.48,257.19,422.77,259.61,423.8,255.77Z"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 426.078px 256.856px;
                    "
                    id="el1g1akiux4ys"
                    class="animable"
                  ></path>
                  <path
                    d="M425.26,255.58s1.86,0,1.75.78c0,0,1.54.2,1.45-.48S425.26,255.58,425.26,255.58Z"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 426.862px 255.931px;
                    "
                    id="el7tgykxvi6ts"
                    class="animable"
                  ></path>
                  <path
                    d="M421.82,262.38a3.38,3.38,0,0,0,2.93,2.05,4.54,4.54,0,0,0,3.41-1.35,6.91,6.91,0,0,0,1.78-3.27c.08-.32.26-1.11-.14-1.32s-.71.31-.93.53a12.59,12.59,0,0,1-2.1,1.68,10.83,10.83,0,0,1-2.38,1.13C424.16,261.91,421.9,262.59,421.82,262.38Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 425.935px 261.437px;
                    "
                    id="elb66m689ih6m"
                    class="animable"
                  ></path>
                  <path
                    d="M431.44,259.47a3,3,0,0,1-.9,2.79,5.33,5.33,0,0,1-1.75,1c-.44.16-1,.29-1.33,0s-.21-.95,0-1.42c.29-.72.59-1.43.92-2.14a7.64,7.64,0,0,1,1-2c.42-.42.84,0,1.28.4A3,3,0,0,1,431.44,259.47Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 429.377px 260.479px;
                    "
                    id="elo16gtl06fth"
                    class="animable"
                  ></path>
                  <path
                    d="M422.58,261.21a2.12,2.12,0,0,1-1.57-1.64c-.11-.59.15-2,.89-2A9.89,9.89,0,0,0,422.58,261.21Z"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 421.783px 259.39px;
                    "
                    id="el73zpyj1ewph"
                    class="animable"
                  ></path>
                  <path
                    d="M428.21,261.62a2.41,2.41,0,0,0,1.89-1.26c.2-.39.44-2.51-.35-1.75-.26.25-.39,1.18-.57,1.53A7.26,7.26,0,0,1,428.21,261.62Z"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 429.254px 260.033px;
                    "
                    id="elsr1bt3r4xl9"
                    class="animable"
                  ></path>
                  <path
                    d="M425.12,262.37a1.74,1.74,0,0,0,2.08.45c-.15.39-1.49.49-1.9.53-1.09.11-1.54-.45-2.46-1.05C422.84,262.3,424.37,262.84,425.12,262.37Z"
                    style="
                      fill: rgb(224, 224, 224);
                      transform-origin: 425.02px 262.832px;
                    "
                    id="elai1vr0sjviw"
                    class="animable"
                  ></path>
                  <polygon
                    points="418.51 299.31 421.07 273.49 424.45 264.32 425.04 264.54 421.67 273.66 419 300.02 418.51 299.31"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 421.775px 282.17px;
                    "
                    id="elddne0ep1r1a"
                    class="animable"
                  ></polygon>
                  <path
                    d="M421.65,273.44l-.56.28a18.66,18.66,0,0,1-1-2.7,22.07,22.07,0,0,0-2.15-5.24l.53-.33a22.74,22.74,0,0,1,2.22,5.38A19,19,0,0,0,421.65,273.44Z"
                    style="
                      fill: rgb(230, 230, 230);
                      transform-origin: 419.795px 269.585px;
                    "
                    id="el8d9hsv1fl0n"
                    class="animable"
                  ></path>
                  <path
                    d="M423,270.05a3.64,3.64,0,0,0,2.32-1.07,7.17,7.17,0,0,0,1.43-2.58c-1.14.12-2.19-.62-3.33-.7a3,3,0,0,0-2.43,1c-.77.9-1.22,2-.8,2.54A3.87,3.87,0,0,0,423,270.05Z"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 423.39px 267.883px;
                    "
                    id="el72bdepbuoto"
                    class="animable"
                  ></path>
                  <path
                    d="M413.88,267.25a4.35,4.35,0,0,1,3.66-.58,3.26,3.26,0,0,1,2,2.22,2.06,2.06,0,0,1-1.95.77,6.14,6.14,0,0,1-2.06-.78,6.3,6.3,0,0,0-2.06-.78Z"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 416.505px 268.091px;
                    "
                    id="eleazngknelpw"
                    class="animable"
                  ></path>
                  <path
                    d="M419.52,267.74c-1.48.17-2.81.46-4.16-1.22-.9-1.13-.61-2.84-.55-4.19a29,29,0,0,1,4.85,2.05A2.38,2.38,0,0,1,421,266a1.38,1.38,0,0,1-1.08,1.54S419.52,267.74,419.52,267.74Z"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 417.866px 265.101px;
                    "
                    id="el1ndu9xqrznj"
                    class="animable"
                  ></path>
                  <path
                    d="M415.28,287.84a12.25,12.25,0,0,0-1,5.29c0,.34.14.73.39.79s.45-.22.53-.53a3.85,3.85,0,0,0,.06-1c0-2.77,1.5-5.11,1.79-7.81.08-.77-.12-3.19-.57-1.41C416.11,284.8,415.83,286.28,415.28,287.84Z"
                    style="
                      fill: rgb(250, 250, 250);
                      transform-origin: 415.67px 288.229px;
                    "
                    id="eldsu1na5j7ng"
                    class="animable"
                  ></path>
                  <path
                    d="M205.77,342.86s2.91-32.21-9.89-47.91,10-1.41,14,14.25c0,0,.75-29-12-47.75s9-4.72,12.79,15.76c0,0,.73-25.86-5.65-39.56s3.13-5.55,7.34,3S214.49,272,214.49,272s4.47-42.1,13-39.82-9.15,31.65-10.56,46c0,0,7.72-20,15.41-17s-10.71,7.24-16.4,36.35L214.24,311s7-19.66,13.36-14.49-15.55,18.06-18,46.87Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 213.105px 286.849px;
                    "
                    id="elr22rd9b82k"
                    class="animable"
                  ></path>
                  <path
                    d="M207.15,344.53s-2.73-39.83,13.48-58.81-12.29-2.05-17.69,17.15c0,0-.16-35.78,16.11-58.54s-11-6.11-16.21,19c0,0-.2-31.92,8-48.63s-3.72-6.95-9.14,3.49-3.45,38.55-3.45,38.55-4.4-52.09-14.93-49.55,10.44,39.34,11.8,57.07c0,0-9-24.92-18.56-21.42s13,9.28,19.25,45.38L197.54,305s-8.08-24.47-16.09-18.31,18.7,22.78,21,58.42Z"
                    style="
                      fill: rgb(240, 240, 240);
                      transform-origin: 199.895px 275.404px;
                    "
                    id="elafnvargobv7"
                    class="animable"
                  ></path>
                  <path
                    d="M232.34,364.39c0,10.93-11.85,19.8-26.47,19.8s-26.48-8.87-26.48-19.8c0-4.93,2.4-9.42,6.38-12.88l-3.13-13.25h46.45L226,351.51C229.94,355,232.34,359.46,232.34,364.39Z"
                    style="
                      fill: rgb(235, 235, 235);
                      transform-origin: 205.865px 361.225px;
                    "
                    id="el8nvwu4k4qes"
                    class="animable"
                  ></path>
                </g>
                <g
                  id="freepik--Shadow--inject-68"
                  class="animable"
                  style="transform-origin: 250px 415.69px"
                >
                  <ellipse
                    id="freepik--path--inject-68"
                    cx="250"
                    cy="415.69"
                    rx="193.89"
                    ry="11.32"
                    style="
                      fill: rgb(245, 245, 245);
                      transform-origin: 250px 415.69px;
                    "
                    class="animable"
                  ></ellipse>
                </g>
                <g
                  id="freepik--Lines--inject-68"
                  class="animable"
                  style="transform-origin: 242.85px 251.335px"
                >
                  <polygon
                    points="234.07 257 236.57 242.58 241.48 244 234.07 257"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 237.775px 249.79px;
                    "
                    id="eljqded912vsl"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="235.72 261.62 249.78 257.55 247.82 252.82 235.72 261.62"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 242.75px 257.22px;
                    "
                    id="el8y168h1tglv"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="238.22 256.19 246.23 241.05 251.63 244.8 238.22 256.19"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 244.925px 248.62px;
                    "
                    id="el3cihe3ozloy"
                    class="animable"
                  ></polygon>
                </g>
                <g
                  id="freepik--Files--inject-68"
                  class="animable animator-active"
                  style="transform-origin: 333.544px 165.856px"
                >
                  <path
                    d="M328.71,115.68H314.14a2.4,2.4,0,0,1,0-4.79h14.57a2.4,2.4,0,0,1,0,4.79Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 321.425px 113.285px;
                    "
                    id="el4aowuf6pavx"
                    class="animable"
                  ></path>
                  <g id="eltxshesw2i1">
                    <g
                      style="
                        opacity: 0.7;
                        transform-origin: 321.425px 113.285px;
                      "
                      class="animable"
                    >
                      <path
                        d="M328.71,115.68H314.14a2.4,2.4,0,0,1,0-4.79h14.57a2.4,2.4,0,0,1,0,4.79Z"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 321.425px 113.285px;
                        "
                        id="elgx3b9l6znk"
                        class="animable"
                      ></path>
                    </g>
                  </g>
                  <path
                    d="M382.16,164.79,326.3,267.59a2.73,2.73,0,0,1-3.7,1.09L227.55,217a2.73,2.73,0,0,1-1.09-3.7L299.11,79.62a2.73,2.73,0,0,1,3.7-1.09l64,34.8Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 304.144px 173.605px;
                    "
                    id="elt70ze6jc41i"
                    class="animable"
                  ></path>
                  <g id="elycn6w2d9co">
                    <g
                      style="
                        opacity: 0.2;
                        transform-origin: 304.144px 173.605px;
                      "
                      class="animable"
                    >
                      <path
                        d="M382.16,164.79,326.3,267.59a2.73,2.73,0,0,1-3.7,1.09L227.55,217a2.73,2.73,0,0,1-1.09-3.7L299.11,79.62a2.73,2.73,0,0,1,3.7-1.09l64,34.8Z"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 304.144px 173.605px;
                        "
                        id="eljvn30kbsjw"
                        class="animable"
                      ></path>
                    </g>
                  </g>
                  <g id="elsz94p2lakam">
                    <rect
                      x="273.81"
                      y="168.41"
                      width="80.66"
                      height="5"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 314.14px 170.91px;
                        transform: rotate(28.35deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="elbheehrfrp4v">
                    <rect
                      x="264.11"
                      y="186.39"
                      width="80.66"
                      height="5"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 304.44px 188.89px;
                        transform: rotate(28.35deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="el8j11iqehd3b">
                    <rect
                      x="254.41"
                      y="204.37"
                      width="80.66"
                      height="5"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 294.74px 206.87px;
                        transform: rotate(28.35deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <path
                    d="M366.94,113.28l-16.84,31a2.73,2.73,0,0,0,1.09,3.7l30.91,16.8Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 365.934px 139.03px;
                    "
                    id="el4gfv0d8b4lu"
                    class="animable"
                  ></path>
                  <g id="elrq78h88ujwa">
                    <path
                      d="M366.94,113.28l-16.84,31a2.73,2.73,0,0,0,1.09,3.7l30.91,16.8Z"
                      style="
                        fill: rgb(255, 255, 255);
                        opacity: 0.7;
                        transform-origin: 365.934px 139.03px;
                      "
                      class="animable"
                    ></path>
                  </g>
                  <path
                    d="M396.72,161.33l-55.85,102.8a2.73,2.73,0,0,1-3.7,1.09l-95.05-51.64a2.73,2.73,0,0,1-1.1-3.7L313.67,76.17a2.73,2.73,0,0,1,3.7-1.1l64.05,34.8Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 318.705px 170.146px;
                    "
                    id="eljem21p3xsmo"
                    class="animable"
                  ></path>
                  <g id="elhjc42w1dgeq">
                    <g
                      style="
                        opacity: 0.5;
                        transform-origin: 318.705px 170.146px;
                      "
                      class="animable"
                    >
                      <path
                        d="M396.72,161.33l-55.85,102.8a2.73,2.73,0,0,1-3.7,1.09l-95.05-51.64a2.73,2.73,0,0,1-1.1-3.7L313.67,76.17a2.73,2.73,0,0,1,3.7-1.1l64.05,34.8Z"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 318.705px 170.146px;
                        "
                        id="elbzpsrzo87e9"
                        class="animable"
                      ></path>
                    </g>
                  </g>
                  <path
                    d="M363.49,183.38l-67.2-36.25a2.14,2.14,0,0,0-2.91.87l-.33.61a2.15,2.15,0,0,0,.87,2.92l67.2,36.25a2.15,2.15,0,0,0,2.91-.87l.33-.62A2.14,2.14,0,0,0,363.49,183.38Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 328.705px 167.453px;
                    "
                    id="elfwbsuv4v5ub"
                    class="animable"
                  ></path>
                  <g id="elchqpp4pn3f">
                    <rect
                      x="278.68"
                      y="182.93"
                      width="80.66"
                      height="5"
                      rx="2.15"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 319.01px 185.43px;
                        transform: rotate(28.35deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="el3elxnrzdy54">
                    <rect
                      x="268.98"
                      y="200.92"
                      width="80.66"
                      height="5"
                      rx="2.15"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 309.31px 203.42px;
                        transform: rotate(28.35deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <path
                    d="M381.51,109.83l-16.85,31a2.71,2.71,0,0,0,1.1,3.69l30.91,16.8Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 380.499px 135.575px;
                    "
                    id="el7lvk0xtewk9"
                    class="animable"
                  ></path>
                  <g id="el4w5ghupa7cs">
                    <path
                      d="M381.51,109.83l-16.85,31a2.71,2.71,0,0,0,1.1,3.69l30.91,16.8Z"
                      style="
                        fill: rgb(255, 255, 255);
                        opacity: 0.7;
                        transform-origin: 380.499px 135.575px;
                      "
                      class="animable"
                    ></path>
                  </g>
                  <path
                    d="M377.65,62.7l4.7,20.87c-17.8,4.88-33.77,22.5-45.26,39.14A96.21,96.21,0,0,0,325.84,145s35.9-32.47,55.69-34.37l-.95,34.49s20.53-40,60.38-54.6C441,90.51,407.58,66.47,377.65,62.7Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 383.4px 103.91px;
                    "
                    id="elrmfzrqkbpa9"
                    class="animable"
                  ></path>
                </g>
                <g
                  id="freepik--Character--inject-68"
                  class="animable"
                  style="transform-origin: 167.321px 313.592px"
                >
                  <g
                    id="freepik--group--inject-68"
                    class="animable"
                    style="transform-origin: 201.016px 290.47px"
                  >
                    <polygon
                      points="252.71 356.93 259.84 351.02 241.86 333.96 234.19 340.51 252.71 356.93"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 247.015px 345.445px;
                      "
                      id="elwt1gru2qrj9"
                      class="animable"
                    ></polygon>
                    <path
                      d="M265.62,348.74a3.82,3.82,0,0,0-2.47.12c-.48.14-1,.31-1.42.47s-.67.26-.94.37l-.79.35a.21.21,0,0,0-.16.21.13.13,0,0,0,0,.1.24.24,0,0,0,.14.1,18,18,0,0,0,3.09.53,3.75,3.75,0,0,0,1.53-.12h.07a4.3,4.3,0,0,0,.82-.37,1.27,1.27,0,0,0,.47-1.11A.77.77,0,0,0,265.62,348.74Zm-.1.66a.76.76,0,0,1-.31.75,1.78,1.78,0,0,1-.81.32,5.07,5.07,0,0,1-1.22.07,13.68,13.68,0,0,1-1.9-.24l-.47-.09a12.81,12.81,0,0,1,2.67-.93A11.71,11.71,0,0,1,265,349a.77.77,0,0,1,.42.1A.28.28,0,0,1,265.52,349.4Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 262.898px 349.805px;
                      "
                      id="elifg2wxr5qg9"
                      class="animable"
                    ></path>
                    <path
                      d="M262.35,345a1.72,1.72,0,0,0-1.13.74,2.32,2.32,0,0,0-.21.38,7.15,7.15,0,0,0-.22,3.6.11.11,0,0,1,0,.05.23.23,0,0,0,.15.17.17.17,0,0,0,.14,0,.11.11,0,0,0,.09-.05,4.73,4.73,0,0,0,.55-.55,8.77,8.77,0,0,0,.85-1.2c.62-1,1.06-2.15.79-2.74C263.26,345.14,263,344.88,262.35,345Zm.6.6c.17.38-.17,1.28-.67,2.16a8.51,8.51,0,0,1-1.08,1.5,6.78,6.78,0,0,1,.14-2.72,1.93,1.93,0,0,1,.26-.54,1.3,1.3,0,0,1,.69-.51l.14,0C262.85,345.37,262.93,345.53,263,345.58Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 262.049px 347.462px;
                      "
                      id="elopsx7dy23pf"
                      class="animable"
                    ></path>
                    <path
                      d="M258.91,350.6l-9,4.52a.79.79,0,0,0-.42.94l2.64,8.38a1.58,1.58,0,0,0,2,1l.15-.07c15.35-5.39,20.06-9.21,21.66-10.08,4.57-2.49,2-5.73.3-5.33-7.66,1.83-10.23,1.36-13.54.51A7.94,7.94,0,0,0,258.91,350.6Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 263.985px 357.724px;
                      "
                      id="el1l79fzrkb0j"
                      class="animable"
                    ></path>
                    <g id="elxngka946m8g">
                      <polygon
                        points="241.87 333.97 250.97 342.04 243.29 348.58 234.19 340.51 241.87 333.97"
                        style="
                          opacity: 0.2;
                          isolation: isolate;
                          transform-origin: 242.58px 341.275px;
                        "
                        class="animable"
                      ></polygon>
                    </g>
                    <polygon
                      points="239.03 348.52 250.48 337.96 247.96 333.54 234.72 344.91 239.03 348.52"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 242.6px 341.03px;
                      "
                      id="elymm281t7q"
                      class="animable"
                    ></polygon>
                    <g id="eli1x6xg1tt2">
                      <polygon
                        points="239.03 348.52 250.48 337.96 247.96 333.54 234.72 344.91 239.03 348.52"
                        style="
                          fill: rgb(255, 255, 255);
                          opacity: 0.5;
                          transform-origin: 242.6px 341.03px;
                        "
                        class="animable"
                      ></polygon>
                    </g>
                    <path
                      d="M246.16,335.09l-1.54,1.32-2.29,2L241,339.54,237,343l-.77.65s-16.31-9.19-25.39-17c-6.21-5.37-6.77-7.38-7.43-6.88-8.77,6.68-34.73,29.74-49.44,41.73-.48.06-1,.1-1.44.14-7.86.57-14-.29-18.84-2.12,0-6.38,5.41-21.28,5.86-22.72,0,0,21.71-21.57,56.89-39.81a11,11,0,0,1,1.06-.47,14.77,14.77,0,0,1,1.38-.56,17.73,17.73,0,0,1,5.39-1.22,11.84,11.84,0,0,1,4.57.72,17.6,17.6,0,0,1,2.44,1.08,20.75,20.75,0,0,1,2,1.18c1.09.69,2.14,1.46,3.13,2.22,2.25,1.74,19.24,23.63,28.37,33.73h0C245.27,334.14,245.73,334.64,246.16,335.09Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 189.925px 328.272px;
                      "
                      id="elq4gmnu2wug"
                      class="animable"
                    ></path>
                    <g id="elirtwff2a1jm">
                      <g
                        style="
                          opacity: 0.1;
                          transform-origin: 189.925px 328.272px;
                        "
                        class="animable"
                      >
                        <path
                          d="M246.16,335.09l-1.54,1.32-2.29,2L241,339.54,237,343l-.77.65s-16.31-9.19-25.39-17c-6.21-5.37-6.77-7.38-7.43-6.88-8.77,6.68-34.73,29.74-49.44,41.73-.48.06-1,.1-1.44.14-7.86.57-14-.29-18.84-2.12,0-6.38,5.41-21.28,5.86-22.72,0,0,21.71-21.57,56.89-39.81a11,11,0,0,1,1.06-.47,14.77,14.77,0,0,1,1.38-.56,17.73,17.73,0,0,1,5.39-1.22,11.84,11.84,0,0,1,4.57.72,17.6,17.6,0,0,1,2.44,1.08,20.75,20.75,0,0,1,2,1.18c1.09.69,2.14,1.46,3.13,2.22,2.25,1.74,19.24,23.63,28.37,33.73h0C245.27,334.14,245.73,334.64,246.16,335.09Z"
                          id="el6a4kcjp5m0l"
                          class="animable"
                          style="transform-origin: 189.925px 328.272px"
                        ></path>
                      </g>
                    </g>
                    <path
                      d="M130.31,243c1.38,6.22,2.82,15.31-1.46,19.59a139.38,139.38,0,0,0,19,25.9c9.37-16.29.49-26.36.49-26.36-7-1.5-6.91-4.33-5.81-9.21Z"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 140.498px 265.745px;
                      "
                      id="ell0bcdhkx1k"
                      class="animable"
                    ></path>
                    <path
                      d="M124.51,263.35a7.9,7.9,0,0,1,3-4.16c1.41-1.07,16-1.23,19.75,0a9.54,9.54,0,0,1,5.29,4.17Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 138.53px 260.843px;
                      "
                      id="elfv547mi1xa8"
                      class="animable"
                    ></path>
                    <path
                      d="M191.68,288.15l3.76-1.72.19,6.14a11.58,11.58,0,0,1-3.69,2.17,2.51,2.51,0,0,1-3.15-3h0A5.38,5.38,0,0,1,191.68,288.15Z"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 192.174px 290.636px;
                      "
                      id="elwjutjcokj9l"
                      class="animable"
                    ></path>
                    <path
                      d="M200.26,288.16l-.2,2.26a1.6,1.6,0,0,1-1.24,1.43l-3.22.72-.19-6.14,3.27.05a1.55,1.55,0,0,1,1.58,1.55Z"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 197.835px 289.5px;
                      "
                      id="el4u2gkz545nn"
                      class="animable"
                    ></path>
                    <path
                      d="M143.87,305.61a32.37,32.37,0,0,0,19.41,3.25c8-1.35,22-9.4,28.07-14l-2-3c-3,.65-27.79,13.23-43.78,1.85-3-2.12-14.69-10.85-18.82-10.67-6.71.3-6.13,7.33-3.25,10.26C126.83,296.65,139.24,303.33,143.87,305.61Z"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 156.404px 296.114px;
                      "
                      id="el6lof06xk4sr"
                      class="animable"
                    ></path>
                    <g id="el6g7n226lnzh">
                      <g
                        style="
                          opacity: 0.2;
                          isolation: isolate;
                          transform-origin: 160.789px 296.058px;
                        "
                        class="animable"
                      >
                        <path
                          d="M200.06,290.42a1.57,1.57,0,0,1-1.23,1.42l-3.2.73h0a11.58,11.58,0,0,1-3.69,2.17,2,2,0,0,1-.59.1h0c-6.08,4.62-20,12.66-28.06,14a32.41,32.41,0,0,1-19.4-3.25c-4.63-2.28-17.06-9-20.43-12.38-2.88-2.93-3.46-10,3.25-10.26,4.13-.18,15.83,8.55,18.82,10.67,15.26,10.85,38.48-.09,43.23-1.69a1.7,1.7,0,0,1,0-.22,5.39,5.39,0,0,1,1-2.12,5.31,5.31,0,0,1,1.85-1.46l3.73-1.71h0l3.25.05a1.55,1.55,0,0,1,1.57,1.55v.14Z"
                          id="eljuchhptw5o"
                          class="animable"
                          style="transform-origin: 160.789px 296.058px"
                        ></path>
                        <polygon
                          points="195.44 286.43 195.41 286.44 195.41 286.43 195.44 286.43"
                          id="elazhlhf0olvc"
                          class="animable"
                          style="transform-origin: 195.425px 286.435px"
                        ></polygon>
                      </g>
                    </g>
                    <path
                      d="M164.84,273.4c8.49,18.71-11.2,24.06-2.18,54.74l-42.8,1c.28-16.44,6.13-12.91-1.58-43.82-.65-2.62-1.73-10.13,1.06-17a12.45,12.45,0,0,1,5.55-6.29c3.16-1.7,17.08-.37,23.43.06C155.2,261.16,163.58,271.06,164.84,273.4Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 142.269px 295.164px;
                      "
                      id="el2doaecosjed"
                      class="animable"
                    ></path>
                    <g id="el0c08mf8hzo95">
                      <path
                        d="M164.84,273.4c8.49,18.71-11.2,24.06-2.18,54.74l-42.8,1c.28-16.44,6.13-12.91-1.58-43.82-.65-2.62-1.73-10.13,1.06-17a12.45,12.45,0,0,1,5.55-6.29c3.16-1.7,17.08-.37,23.43.06C155.2,261.16,163.58,271.06,164.84,273.4Z"
                        style="
                          fill: rgb(255, 255, 255);
                          opacity: 0.5;
                          transform-origin: 142.269px 295.164px;
                        "
                        class="animable"
                      ></path>
                    </g>
                    <path
                      d="M156.66,236.28c-.12.82.21,1.49.72,1.56s1-.5,1.15-1.29-.22-1.48-.73-1.56S156.77,235.5,156.66,236.28Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 157.6px 236.414px;
                      "
                      id="el1b7xg0o2rdf"
                      class="animable"
                    ></path>
                    <path
                      d="M157.57,235l2-.27S158.35,236.07,157.57,235Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 158.57px 235.072px;
                      "
                      id="elhipr87nca2j"
                      class="animable"
                    ></path>
                    <path
                      d="M156.79,237.36a20.74,20.74,0,0,0,2.08,5.41,3.41,3.41,0,0,1-2.88.12Z"
                      style="
                        fill: rgb(160, 39, 36);
                        transform-origin: 157.43px 240.256px;
                      "
                      id="elgzkmkamwi6j"
                      class="animable"
                    ></path>
                    <path
                      d="M159.49,230.78a.45.45,0,0,0,.29-.36.48.48,0,0,0-.39-.54,4.62,4.62,0,0,0-4.06,1.28.47.47,0,1,0,.63.69l.06-.07a3.73,3.73,0,0,1,3.23-1A.48.48,0,0,0,159.49,230.78Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 157.461px 230.91px;
                      "
                      id="el19ub0o9xyk7"
                      class="animable"
                    ></path>
                    <path
                      d="M130.76,229.8c-.81,9.75-1.36,13.86,2.79,19.53,6.26,8.52,18.43,7.4,22.11-1.91,3.35-8.39,4.11-22.92-4.78-28.13A13.34,13.34,0,0,0,132.59,224,13.2,13.2,0,0,0,130.76,229.8Z"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 144.09px 236.269px;
                      "
                      id="el2hqe8oa0uu6"
                      class="animable"
                    ></path>
                    <path
                      d="M155.89,246.83a5.51,5.51,0,0,1-1.62-2.39.23.23,0,0,1,.14-.25.2.2,0,0,1,.24.14,5.44,5.44,0,0,0,1.39,2.09Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 155.153px 245.507px;
                      "
                      id="elgeebvwe8om"
                      class="animable"
                    ></path>
                    <path
                      d="M123.81,217.13c-3.71,5-5.4,6.34-.8,19.75,1.85,5.39,7.22,12.53,9.83,13.18,4.68,1.18,9.23-2.1,12.74-5.41a35.71,35.71,0,0,0,7.9-9.82c1.88-3.79,2.57-8.34,1-12.27-1.68-4.27-7.61-8.08-12.05-9C137.23,212.44,126.9,212.94,123.81,217.13Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 137.788px 231.675px;
                      "
                      id="elrrfq8as7gte"
                      class="animable"
                    ></path>
                    <path
                      d="M153,235.66s1.17,2-.31,3.51l0-2.67Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 153.065px 237.415px;
                      "
                      id="elhdl9lo17hig"
                      class="animable"
                    ></path>
                    <path
                      d="M153,235.66s.43,3.08-2.15,4.23l1.38-3.32Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 151.938px 237.775px;
                      "
                      id="elv5r3z4vqm4"
                      class="animable"
                    ></path>
                    <path
                      d="M135.78,248.93s-2.84,1.29-2.43,4.08l2.07-2.95Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 134.545px 250.97px;
                      "
                      id="elohhuihs3mim"
                      class="animable"
                    ></path>
                    <path
                      d="M135.89,249s-2.16,2.24-.74,4.69l.83-3.51Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 135.323px 251.345px;
                      "
                      id="el8tb1h5im3hd"
                      class="animable"
                    ></path>
                    <path
                      d="M156.86,231.63a18.54,18.54,0,0,0,2.78-3.35,6.28,6.28,0,0,0,1-4.16,6.42,6.42,0,0,0-3.32-4.33A18.6,18.6,0,0,0,152,218a3.69,3.69,0,0,0-2.7.08,2.51,2.51,0,0,0-1,2.32,8,8,0,0,0,.72,2.56,52.75,52.75,0,0,1,2.68,10c.31,1.72.08,2.87,1.78,2.2C154.53,234.77,156,232.54,156.86,231.63Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 154.48px 226.568px;
                      "
                      id="el1yuh2xaqyep"
                      class="animable"
                    ></path>
                    <path
                      d="M143.4,236.45a8.53,8.53,0,0,0,2.21,6.13c2,2.2,4.62.76,5.36-2,.67-2.46.42-6.57-2.25-7.75S143.54,233.7,143.4,236.45Z"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 147.338px 238.071px;
                      "
                      id="elmxe87sh4k6g"
                      class="animable"
                    ></path>
                    <polygon
                      points="256.82 361.42 264.54 353.9 249.59 335.11 240.26 340.62 256.82 361.42"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 252.4px 348.265px;
                      "
                      id="eleeoe4el07cm"
                      class="animable"
                    ></polygon>
                    <path
                      d="M272.42,351.58c-.85-.3-2.61.66-3.95,1.51-.34.21-.64.42-.9.6h0l-.13.1c-.3.21-.52.37-.6.44a.22.22,0,0,0-.12.25.25.25,0,0,0,.23.18,18.23,18.23,0,0,0,2.76-.09l.61-.07a3.84,3.84,0,0,0,1.85-.64,3.33,3.33,0,0,0,.56-.43,1.35,1.35,0,0,0,.25-1.27A.88.88,0,0,0,272.42,351.58Zm.06.72a.88.88,0,0,1-.17.86,2.83,2.83,0,0,1-1.52.76,11,11,0,0,1-2.06.27q-.48,0-1,0l.34-.25a1.77,1.77,0,0,1,.24-.17,13,13,0,0,1,3.51-1.75.84.84,0,0,1,.47,0A.32.32,0,0,1,272.48,352.3Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 269.878px 353.1px;
                      "
                      id="el4zmz5tzdbpp"
                      class="animable"
                    ></path>
                    <path
                      d="M268.14,348.39a1.74,1.74,0,0,0-1,1c-.64,1.53.3,3.91.45,4.28h0a0,0,0,0,0,0,0,.25.25,0,0,0,.2.15.38.38,0,0,0,.15,0,.14.14,0,0,0,.08-.07l0,0a5.05,5.05,0,0,0,.42-.68c.74-1.39,1.43-3.71.83-4.51C269.12,348.34,268.79,348.12,268.14,348.39Zm-.25,4.72a5.79,5.79,0,0,1-.32-3.51,1.34,1.34,0,0,1,.62-.69l.13-.06c.43-.17.54,0,.58,0C269.34,349.46,268.67,351.83,267.89,353.11Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 268.209px 351.046px;
                      "
                      id="el6wkefe9vext"
                      class="animable"
                    ></path>
                    <g id="el590oqk20xfr">
                      <polygon
                        points="248.81 333.96 255.84 342.96 246.33 348.27 239.19 339.5 248.81 333.96"
                        style="
                          opacity: 0.2;
                          isolation: isolate;
                          transform-origin: 247.515px 341.115px;
                        "
                        class="animable"
                      ></polygon>
                    </g>
                    <path
                      d="M119.47,325.89l-1,3.89c-.15.3.22.59.71.58l44.07-1c.39,0,.7-.21.72-.46l-1.1-4.07c0-.26-.32-.48-.74-.47l-42,1.24A.81.81,0,0,0,119.47,325.89Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 141.203px 327.36px;
                      "
                      id="elp0k9ia35md"
                      class="animable"
                    ></path>
                    <path
                      d="M158.69,329.78l-1.16.13c-.23,0-.42-.07-.42-.22l0-5c0-.15.19-.29.41-.31l1.16-.14c.23,0,.42.08.42.23l0,5C159.1,329.62,158.92,329.76,158.69,329.78Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 158.105px 327.075px;
                      "
                      id="elpaljofc971"
                      class="animable"
                    ></path>
                    <path
                      d="M142.91,330l-1.16.12c-.22,0-.41-.07-.41-.22l0-5c0-.14.19-.28.42-.31l1.15-.13c.23,0,.42.07.42.22l0,5C143.33,329.84,143.14,330,142.91,330Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 142.335px 327.29px;
                      "
                      id="ele5zwra8vl0d"
                      class="animable"
                    ></path>
                    <path
                      d="M142.91,330l-1.16.12c-.22,0-.41-.07-.41-.22l0-5c0-.14.19-.28.42-.31l1.15-.13c.23,0,.42.07.42.22l0,5C143.33,329.84,143.14,330,142.91,330Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 142.335px 327.29px;
                      "
                      id="elsrrt8n2gd6"
                      class="animable"
                    ></path>
                    <path
                      d="M254.72,338l-1.95,1.1h0L249.41,341l-3,1.69h0l-3.09,1.74h0l-1.19.67-.74-.55c-.18-.12-.39-.27-.63-.46-.74-.55-1.76-1.31-3-2.26h0c-6.21-4.92-17.28-14.58-20.58-23.37-2.13,2.54-4.68,5.73-7.6,9.25C197,342.88,177.48,364.29,154,367.08l-1.44.15c-7.85.67-14-.11-18.85-1.88-12.19-4.47-15.59-15.18-14.76-24.29v0c.08-4.27.91-11.87.91-11.87l44.48,0c6.26-7.61,18.84-19.53,31.69-27,.3-.19.61-.37.92-.53s.77-.44,1.15-.65a51.81,51.81,0,0,1,12.33-5c.88-.21,1.75-.39,2.61-.52a24.37,24.37,0,0,1,2.66-.25h0c6.09-.27,11.38,2,15,8.07L254.05,337Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.776px 331.343px;
                      "
                      id="elvddy5fi0o7"
                      class="animable"
                    ></path>
                    <g
                      id="freepik--monitor-screen--inject-68"
                      class="animable"
                      style="transform-origin: 206.765px 277.21px"
                    >
                      <g
                        id="freepik--PC--inject-68"
                        class="animable"
                        style="transform-origin: 206.765px 277.21px"
                      >
                        <polygon
                          points="230.72 291.78 181.58 293.81 183.02 262.54 232.16 260.51 230.72 291.78"
                          style="
                            fill: rgb(64, 123, 255);
                            transform-origin: 206.87px 277.16px;
                          "
                          id="el7p0t5saw9i"
                          class="animable"
                        ></polygon>
                        <path
                          d="M230.15,294.24l-48.43,2a2.23,2.23,0,0,1-2.37-2.39l1.42-31.07a2.78,2.78,0,0,1,2.61-2.6l48.43-2a2.24,2.24,0,0,1,2.37,2.39l-1.43,31.07A2.76,2.76,0,0,1,230.15,294.24Z"
                          style="
                            fill: rgb(38, 50, 56);
                            transform-origin: 206.765px 277.21px;
                          "
                          id="el0tx8xrg6cpca"
                          class="animable"
                        ></path>
                        <polygon
                          points="230.72 291.78 181.58 293.81 183.02 262.54 232.16 260.51 230.72 291.78"
                          style="
                            fill: rgb(64, 123, 255);
                            transform-origin: 206.87px 277.16px;
                          "
                          id="elv4juwv0w9xa"
                          class="animable"
                        ></polygon>
                        <g id="eladiyb3149f5">
                          <polygon
                            points="230.72 291.78 181.58 293.81 183.02 262.54 232.16 260.51 230.72 291.78"
                            style="
                              fill: rgb(255, 255, 255);
                              opacity: 0.9;
                              transform-origin: 206.87px 277.16px;
                            "
                            class="animable"
                          ></polygon>
                        </g>
                        <g id="elcj6tvl2rcgw">
                          <polygon
                            points="200.46 259.49 192.34 295.79 195.57 295.66 203.58 259.36 200.46 259.49"
                            style="
                              fill: rgb(255, 255, 255);
                              opacity: 0.1;
                              isolation: isolate;
                              transform-origin: 197.96px 277.575px;
                            "
                            class="animable"
                          ></polygon>
                        </g>
                        <g id="elnp4gs2g2jz">
                          <polygon
                            points="205.44 259.28 197.32 295.58 203.73 295.32 211.74 259.02 205.44 259.28"
                            style="
                              fill: rgb(255, 255, 255);
                              opacity: 0.1;
                              isolation: isolate;
                              transform-origin: 204.53px 277.3px;
                            "
                            class="animable"
                          ></polygon>
                        </g>
                      </g>
                    </g>
                    <path
                      d="M214.77,294.63l16.36-.46c.28,1.9-.53,2.61-1.57,2.64l-5.23.13-3.5.08-5.43.15-33.69,1-.27-2.37Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 206.313px 296.17px;
                      "
                      id="el3217f0vbgts"
                      class="animable"
                    ></path>
                    <path
                      d="M214.77,294.63l16.36-.46c.28,1.9-.53,2.61-1.57,2.64l-5.23.13-3.5.08-5.43.15-41.7,1.28a1.2,1.2,0,0,1-1.13-.68h0a1.21,1.21,0,0,1,1.05-1.73Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 201.819px 296.311px;
                      "
                      id="el7j18a9j8os6"
                      class="animable"
                    ></path>
                    <g id="elzhh8wdxer1j">
                      <path
                        d="M214.77,294.63l16.36-.46c.28,1.9-.53,2.61-1.57,2.64l-5.23.13-3.5.08-5.43.15-41.7,1.28a1.2,1.2,0,0,1-1.13-.68h0a1.21,1.21,0,0,1,1.05-1.73Z"
                        style="
                          opacity: 0.2;
                          transform-origin: 201.819px 296.311px;
                        "
                        class="animable"
                      ></path>
                    </g>
                    <g id="el2f71845whau">
                      <path
                        d="M231.13,294.17l.1.66a1.73,1.73,0,0,1-1.67,2l-5.23.13-9.72.35.16-2.66Z"
                        style="
                          opacity: 0.2;
                          transform-origin: 222.931px 295.74px;
                        "
                        class="animable"
                      ></path>
                    </g>
                    <g id="el85ggiqynvsb">
                      <path
                        d="M146.39,274.32s-2.31,4.71,4.36,17.15l2.79,5.07h0c.92,1.67,7-1.74,8.86-4.87h0S150.7,284.65,146.39,274.32Z"
                        style="
                          opacity: 0.2;
                          transform-origin: 154.202px 285.65px;
                        "
                        class="animable"
                      ></path>
                    </g>
                    <path
                      d="M203,288.82l4.65-1.37-.74,7.18s-6.49,4.34-8.74.19l.91-2.31A6.22,6.22,0,0,1,203,288.82Z"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 202.91px 292.033px;
                      "
                      id="elh9jn70saumd"
                      class="animable"
                    ></path>
                    <path
                      d="M213,290.27l-.58,2.59a1.86,1.86,0,0,1-1.67,1.46l-3.87.31.75-7.19,3.8.6a1.86,1.86,0,0,1,1.6,2.08Z"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 209.963px 291.035px;
                      "
                      id="eln23bjmc9r1m"
                      class="animable"
                    ></path>
                    <path
                      d="M164.24,301c3.25,4.4,7.81,8.08,13.17,9.13,6.32,1.23,18.48-7.71,24.18-13.49-.28-2.44-.12-3.76-2.55-4.1,0,0-6.28,4.6-18.11,7.36-3.83.89-6.38-3-9.71-8.71-1.66-2.83-7-14.47-9.07-17.06-3.26-4.16-12.52-1.18-8.84,8.83C154.85,287.14,161.59,297.38,164.24,301Z"
                      style="
                        fill: rgb(203, 122, 99);
                        transform-origin: 177.025px 291.277px;
                      "
                      id="elxki2ceuvz1d"
                      class="animable"
                    ></path>
                    <path
                      d="M160.78,267.29c6.57,6,9.77,16.72,9.77,16.72l-15.35,9.36S144,277.61,146,272.12c1.58-4.26,4.51-7.06,8.36-7.3A8.82,8.82,0,0,1,160.78,267.29Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 158.155px 279.093px;
                      "
                      id="ellijebyqj0o"
                      class="animable"
                    ></path>
                    <path
                      d="M125.56,330.59l-1.16,0c-.23,0-.42-.11-.4-.26l.43-5c0-.15.21-.27.44-.28l1.16,0c.23,0,.42.12.4.26l-.43,5A.38.38,0,0,1,125.56,330.59Z"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 125.215px 327.823px;
                      "
                      id="eljv0hr2y74t"
                      class="animable"
                    ></path>
                    <polygon
                      points="240.23 347.23 255.19 339.75 253.91 334.43 236.85 342.21 240.23 347.23"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 246.02px 340.83px;
                      "
                      id="elolpp0ovq1m"
                      class="animable"
                    ></polygon>
                    <g id="elyyp58vs3nvh">
                      <polygon
                        points="240.23 347.23 255.19 339.75 253.91 334.43 236.85 342.21 240.23 347.23"
                        style="
                          fill: rgb(255, 255, 255);
                          opacity: 0.5;
                          transform-origin: 246.02px 340.83px;
                        "
                        class="animable"
                      ></polygon>
                    </g>
                    <path
                      d="M263.94,353.08l-10.32,3.12a.85.85,0,0,0-.62.92l1.25,9.36a1.68,1.68,0,0,0,1.95,1.39l.18,0c17.24-2.87,22.93-6,24.78-6.66,5.3-1.79,3.18-5.69,1.3-5.58-8.44.52-11.07-.46-14.42-2A8.45,8.45,0,0,0,263.94,353.08Z"
                      style="
                        fill: rgb(38, 50, 56);
                        transform-origin: 268.753px 360.46px;
                      "
                      id="elfiasxdbjvw8"
                      class="animable"
                    ></path>
                  </g>
                  <path
                    d="M125.17,229.69c-3.1.49-6.17-1.89-7.14-4.87a11.29,11.29,0,0,1,1.43-9c1.17-2,8.84-6.74,11.68-1.4C136.8,225,125.17,229.69,125.17,229.69Z"
                    style="
                      fill: rgb(38, 50, 56);
                      transform-origin: 125.175px 220.86px;
                    "
                    id="elcrovaw6lxv"
                    class="animable"
                  ></path>
                  <polygon
                    points="230.28 271.23 200.03 272.51 200.17 269.51 230.42 268.23 230.28 271.23"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 215.225px 270.37px;
                    "
                    id="elq0k53sjgtp7"
                    class="animable"
                  ></polygon>
                  <g id="elkgpp5z3acp">
                    <g
                      style="opacity: 0.7; transform-origin: 215.225px 270.37px"
                      class="animable"
                    >
                      <polygon
                        points="230.28 271.23 200.03 272.51 200.17 269.51 230.42 268.23 230.28 271.23"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 215.225px 270.37px;
                        "
                        id="elob4mwkvt8k"
                        class="animable"
                      ></polygon>
                    </g>
                  </g>
                  <polygon
                    points="230.1 275.39 199.85 276.68 199.98 273.68 230.23 272.39 230.1 275.39"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 215.04px 274.535px;
                    "
                    id="elkk3kym43s"
                    class="animable"
                  ></polygon>
                  <g id="el0u1lk9hqeq1">
                    <g
                      style="opacity: 0.7; transform-origin: 215.04px 274.535px"
                      class="animable"
                    >
                      <polygon
                        points="230.1 275.39 199.85 276.68 199.98 273.68 230.23 272.39 230.1 275.39"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 215.04px 274.535px;
                        "
                        id="el00q06ab8rwf4"
                        class="animable"
                      ></polygon>
                    </g>
                  </g>
                  <polygon
                    points="229.91 279.56 199.66 280.85 199.8 277.84 230.04 276.56 229.91 279.56"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 214.85px 278.705px;
                    "
                    id="elefad4vlyyel"
                    class="animable"
                  ></polygon>
                  <g id="eltzheuohcji9">
                    <g
                      style="opacity: 0.7; transform-origin: 214.85px 278.705px"
                      class="animable"
                    >
                      <polygon
                        points="229.91 279.56 199.66 280.85 199.8 277.84 230.04 276.56 229.91 279.56"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 214.85px 278.705px;
                        "
                        id="el94wt63ayf5q"
                        class="animable"
                      ></polygon>
                    </g>
                  </g>
                  <polygon
                    points="229.72 283.72 199.47 285.01 199.61 282.01 229.86 280.72 229.72 283.72"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 214.665px 282.865px;
                    "
                    id="el56q3h9ep82w"
                    class="animable"
                  ></polygon>
                  <g id="elxw56mvsjeqo">
                    <g
                      style="
                        opacity: 0.7;
                        transform-origin: 214.665px 282.865px;
                      "
                      class="animable"
                    >
                      <polygon
                        points="229.72 283.72 199.47 285.01 199.61 282.01 229.86 280.72 229.72 283.72"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 214.665px 282.865px;
                        "
                        id="elv1f263lfww"
                        class="animable"
                      ></polygon>
                    </g>
                  </g>
                  <polygon
                    points="229.54 287.89 199.29 289.18 199.42 286.18 229.67 284.89 229.54 287.89"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 214.48px 287.035px;
                    "
                    id="elgoolwnzz95a"
                    class="animable"
                  ></polygon>
                  <g id="elolpb273ohx">
                    <g
                      style="opacity: 0.7; transform-origin: 214.48px 287.035px"
                      class="animable"
                    >
                      <polygon
                        points="229.54 287.89 199.29 289.18 199.42 286.18 229.67 284.89 229.54 287.89"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 214.48px 287.035px;
                        "
                        id="el2gppflvyi2v"
                        class="animable"
                      ></polygon>
                    </g>
                  </g>
                  <g id="elcdjmnagga6m">
                    <rect
                      x="185.4"
                      y="274.25"
                      width="2.43"
                      height="1"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.615px 274.75px;
                        transform: rotate(-2.46deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="elv212670v7em">
                    <g
                      style="opacity: 0.5; transform-origin: 186.615px 274.75px"
                      class="animable"
                    >
                      <g id="ela16wptifmv5">
                        <rect
                          x="185.4"
                          y="274.25"
                          width="2.43"
                          height="1"
                          style="
                            fill: rgb(255, 255, 255);
                            transform-origin: 186.615px 274.75px;
                            transform: rotate(-2.46deg);
                          "
                          class="animable"
                        ></rect>
                      </g>
                    </g>
                  </g>
                  <g id="elktf3gjpry6">
                    <rect
                      x="185.29"
                      y="277.14"
                      width="2.43"
                      height="1"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.505px 277.64px;
                        transform: rotate(-2.46deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="elborfqnba8rp">
                    <g
                      style="opacity: 0.5; transform-origin: 186.505px 277.64px"
                      class="animable"
                    >
                      <g id="elhak2yio163o">
                        <rect
                          x="185.29"
                          y="277.14"
                          width="2.43"
                          height="1"
                          style="
                            fill: rgb(255, 255, 255);
                            transform-origin: 186.505px 277.64px;
                            transform: rotate(-2.46deg);
                          "
                          class="animable"
                        ></rect>
                      </g>
                    </g>
                  </g>
                  <g id="elzc6zd74buq">
                    <rect
                      x="185.17"
                      y="280.02"
                      width="2.43"
                      height="1"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.385px 280.52px;
                        transform: rotate(-2.29061deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="elgxgqo13gkig">
                    <g
                      style="opacity: 0.5; transform-origin: 186.385px 280.52px"
                      class="animable"
                    >
                      <g id="el4rfvq73e00m">
                        <rect
                          x="185.17"
                          y="280.02"
                          width="2.43"
                          height="1"
                          style="
                            fill: rgb(255, 255, 255);
                            transform-origin: 186.385px 280.52px;
                            transform: rotate(-2.29061deg);
                          "
                          class="animable"
                        ></rect>
                      </g>
                    </g>
                  </g>
                  <g id="elbmz41c3y0gh">
                    <rect
                      x="185.06"
                      y="282.91"
                      width="2.43"
                      height="1"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.275px 283.41px;
                        transform: rotate(-2.46deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="el62ouqgc6qc6">
                    <g
                      style="opacity: 0.5; transform-origin: 186.275px 283.41px"
                      class="animable"
                    >
                      <g id="elowslmkdm3r">
                        <rect
                          x="185.06"
                          y="282.91"
                          width="2.43"
                          height="1"
                          style="
                            fill: rgb(255, 255, 255);
                            transform-origin: 186.275px 283.41px;
                            transform: rotate(-2.46deg);
                          "
                          class="animable"
                        ></rect>
                      </g>
                    </g>
                  </g>
                  <g id="elpno1sbagcn">
                    <rect
                      x="184.94"
                      y="285.79"
                      width="2.43"
                      height="1"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.155px 286.29px;
                        transform: rotate(-2.29061deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="elce89xw5c8s5">
                    <g
                      style="
                        opacity: 0.5;
                        transform-origin: 186.225px 286.285px;
                      "
                      class="animable"
                    >
                      <polygon
                        points="184.97 286.84 185.06 285.84 187.48 285.73 187.39 286.74 184.97 286.84"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 186.225px 286.285px;
                        "
                        id="eloeu7vl8hb6"
                        class="animable"
                      ></polygon>
                    </g>
                  </g>
                  <g id="elu7taikfahm">
                    <rect
                      x="184.83"
                      y="288.68"
                      width="2.43"
                      height="1"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.045px 289.18px;
                        transform: rotate(-2.41deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="elgmv3dwss2gk">
                    <g
                      style="opacity: 0.5; transform-origin: 186.045px 289.18px"
                      class="animable"
                    >
                      <g id="elcdqaqbllc9h">
                        <rect
                          x="184.83"
                          y="288.68"
                          width="2.43"
                          height="1"
                          style="
                            fill: rgb(255, 255, 255);
                            transform-origin: 186.045px 289.18px;
                            transform: rotate(-2.41deg);
                          "
                          class="animable"
                        ></rect>
                      </g>
                    </g>
                  </g>
                  <polygon
                    points="190.34 271.44 185.32 273.31 185.37 271.99 188.15 271.54 185.4 271.35 185.45 270.03 190.34 271.44"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 187.83px 271.67px;
                    "
                    id="elt60y897k6j"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="220.99 266.67 200.03 267.56 200.13 265.48 221.09 264.59 220.99 266.67"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 210.56px 266.075px;
                    "
                    id="el2oqchyz9zjp"
                    class="animable"
                  ></polygon>
                  <g id="elx7f37rrj5kg">
                    <g
                      style="opacity: 0.7; transform-origin: 210.56px 266.075px"
                      class="animable"
                    >
                      <polygon
                        points="220.99 266.67 200.03 267.56 200.13 265.48 221.09 264.59 220.99 266.67"
                        style="
                          fill: rgb(255, 255, 255);
                          transform-origin: 210.56px 266.075px;
                        "
                        id="el4iluv0ws3m"
                        class="animable"
                      ></polygon>
                    </g>
                  </g>
                  <polygon
                    points="192.71 267.74 189.64 267.88 190.88 267.09 191.22 267.4 191.59 267.08 192.71 267.74"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 191.175px 267.48px;
                    "
                    id="elswrlpwmuip"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="190.76 266.99 189.52 267.79 189.61 265.95 190.76 266.99"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 190.14px 266.87px;
                    "
                    id="el4kb7xu80k98"
                    class="animable"
                  ></polygon>
                  <polygon
                    points="192.91 265.9 192.81 267.63 191.68 266.97 192.91 265.9"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 192.295px 266.765px;
                    "
                    id="eli47btvf5x0d"
                    class="animable"
                  ></polygon>
                  <g id="elpodyf5p97s">
                    <rect
                      x="191.18"
                      y="266.7"
                      width="0.1"
                      height="0.01"
                      style="
                        fill: rgb(255, 255, 255);
                        transform-origin: 191.23px 266.705px;
                        transform: rotate(-46.6deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="elmxzea2pnqwc">
                    <rect
                      x="191.23"
                      y="266.66"
                      width="0.01"
                      height="0.1"
                      style="
                        fill: rgb(255, 255, 255);
                        transform-origin: 191.235px 266.71px;
                        transform: rotate(-43.45deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <polygon
                    points="192.91 265.72 191.59 266.92 191.22 267.25 190.88 266.93 189.73 265.89 189.64 265.81 192.91 265.72"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 191.275px 266.485px;
                    "
                    id="el2i2yogh1ivm"
                    class="animable"
                  ></polygon>
                  <g id="ell7ptz4uh8d">
                    <rect
                      x="185.4"
                      y="266.11"
                      width="2.43"
                      height="0.3"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.615px 266.26px;
                        transform: rotate(-2.43deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="elnxwsijh6z5r">
                    <rect
                      x="185.4"
                      y="266.87"
                      width="2.43"
                      height="0.3"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.615px 267.02px;
                        transform: rotate(-2.43deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <g id="elw7ntcvj0dx">
                    <rect
                      x="185.4"
                      y="267.64"
                      width="2.43"
                      height="0.3"
                      style="
                        fill: rgb(64, 123, 255);
                        transform-origin: 186.615px 267.79px;
                        transform: rotate(-2.43deg);
                      "
                      class="animable"
                    ></rect>
                  </g>
                  <path
                    d="M135.51,290.7l9.07,103.68H130l-9.76-111.57h6.7A8.64,8.64,0,0,1,135.51,290.7Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 132.41px 338.595px;
                    "
                    id="el1h5iijbk9vo"
                    class="animable"
                  ></path>
                  <g id="eljn0ec4l8s9r">
                    <path
                      d="M135.6,291.64l9,102.74H130l-9.76-111.57H126A9.68,9.68,0,0,1,135.6,291.64Z"
                      style="opacity: 0.2; transform-origin: 132.42px 338.595px"
                      class="animable"
                    ></path>
                  </g>
                  <path
                    d="M126,289.57l9.17,104.81h-87l-9-103.52a7.4,7.4,0,0,1,7.37-8.05h72.18A7.4,7.4,0,0,1,126,289.57Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 87.1557px 338.595px;
                    "
                    id="elsu8nooimv7r"
                    class="animable"
                  ></path>
                  <g id="elxmbchg3h1l">
                    <path
                      d="M126.11,290.71l9.07,103.67h-87L39.21,292.22a8.65,8.65,0,0,1,8.61-9.41H117.5A8.65,8.65,0,0,1,126.11,290.71Z"
                      style="
                        fill: rgb(255, 255, 255);
                        opacity: 0.2;
                        transform-origin: 87.1783px 338.595px;
                      "
                      class="animable"
                    ></path>
                  </g>
                  <path
                    d="M279.19,394.38H48.54L46,365.63h221.4a10.3,10.3,0,0,1,10.06,9.25Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 162.595px 380.005px;
                    "
                    id="elw3kkhic38ts"
                    class="animable"
                  ></path>
                  <g id="elz0gb8aorui">
                    <path
                      d="M279.19,394.38H48.54L46,365.63h221.4a10.3,10.3,0,0,1,10.06,9.25Z"
                      style="
                        fill: rgb(255, 255, 255);
                        opacity: 0.2;
                        transform-origin: 162.595px 380.005px;
                      "
                      class="animable"
                    ></path>
                  </g>
                  <path
                    d="M289.77,405.39H45.83a5.74,5.74,0,0,1-5.73-5.73h0a5.73,5.73,0,0,1,5.73-5.73H289.77a5.73,5.73,0,0,1,5.73,5.73h0A5.74,5.74,0,0,1,289.77,405.39Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 167.8px 399.66px;
                    "
                    id="elqcvc4e57y9m"
                    class="animable"
                  ></path>
                  <g id="elmqty342a6m">
                    <path
                      d="M289.77,405.39H148.16a5.73,5.73,0,0,1-5.73-5.73h0a5.72,5.72,0,0,1,5.73-5.73H289.77a5.73,5.73,0,0,1,5.73,5.73h0A5.74,5.74,0,0,1,289.77,405.39Z"
                      style="opacity: 0.2; transform-origin: 218.965px 399.66px"
                      class="animable"
                    ></path>
                  </g>
                  <polygon
                    points="49.03 405.39 51.92 415.22 57.7 415.22 60.88 405.39 49.03 405.39"
                    style="
                      fill: rgb(38, 50, 56);
                      transform-origin: 54.955px 410.305px;
                    "
                    id="elun6fwf1giil"
                    class="animable"
                  ></polygon>
                  <g id="eluxkyokt9cf">
                    <polygon
                      points="49.03 405.39 51.92 415.22 57.7 415.22 60.88 405.39 49.03 405.39"
                      style="
                        fill: rgb(255, 255, 255);
                        opacity: 0.5;
                        transform-origin: 54.955px 410.305px;
                      "
                      class="animable"
                    ></polygon>
                  </g>
                  <polygon
                    points="131.86 405.39 134.75 415.22 140.53 415.22 143.72 405.39 131.86 405.39"
                    style="
                      fill: rgb(38, 50, 56);
                      transform-origin: 137.79px 410.305px;
                    "
                    id="el33qm5c1vpto"
                    class="animable"
                  ></polygon>
                  <g id="eln2t2api38yb">
                    <polygon
                      points="131.86 405.39 134.75 415.22 140.53 415.22 143.72 405.39 131.86 405.39"
                      style="
                        fill: rgb(255, 255, 255);
                        opacity: 0.5;
                        transform-origin: 137.79px 410.305px;
                      "
                      class="animable"
                    ></polygon>
                  </g>
                  <polygon
                    points="195.26 405.39 198.15 415.22 203.93 415.22 207.11 405.39 195.26 405.39"
                    style="
                      fill: rgb(38, 50, 56);
                      transform-origin: 201.185px 410.305px;
                    "
                    id="el9mhogv4eo28"
                    class="animable"
                  ></polygon>
                  <g id="elz2uod6x1q">
                    <polygon
                      points="195.26 405.39 198.15 415.22 203.93 415.22 207.11 405.39 195.26 405.39"
                      style="
                        fill: rgb(255, 255, 255);
                        opacity: 0.5;
                        transform-origin: 201.185px 410.305px;
                      "
                      class="animable"
                    ></polygon>
                  </g>
                  <polygon
                    points="278.09 405.39 280.98 415.22 286.76 415.22 289.94 405.39 278.09 405.39"
                    style="
                      fill: rgb(38, 50, 56);
                      transform-origin: 284.015px 410.305px;
                    "
                    id="el7yyirdis36p"
                    class="animable"
                  ></polygon>
                  <g id="el4jfsvny8ufl">
                    <polygon
                      points="278.09 405.39 280.98 415.22 286.76 415.22 289.94 405.39 278.09 405.39"
                      style="
                        fill: rgb(255, 255, 255);
                        opacity: 0.5;
                        transform-origin: 284.015px 410.305px;
                      "
                      class="animable"
                    ></polygon>
                  </g>
                  <path
                    d="M105.89,278.91H99.56a.5.5,0,0,1-.5-.5.5.5,0,0,1,.5-.5h6.33a.51.51,0,0,1,.5.5A.5.5,0,0,1,105.89,278.91Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 102.725px 278.41px;
                    "
                    id="el628bfnxkcul"
                    class="animable"
                  ></path>
                  <path
                    d="M95.35,278.91H63.62a.5.5,0,0,1-.5-.5.51.51,0,0,1,.5-.5H95.35a.51.51,0,0,1,.5.5A.5.5,0,0,1,95.35,278.91Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 79.485px 278.41px;
                    "
                    id="elbc7d5ma2g6"
                    class="animable"
                  ></path>
                  <path
                    d="M207.85,336.78a.55.55,0,0,1-.34-.13.5.5,0,0,1,0-.71l3-3.22a.5.5,0,0,1,.71,0,.51.51,0,0,1,0,.71l-3,3.22A.52.52,0,0,1,207.85,336.78Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 209.363px 334.676px;
                    "
                    id="el3yiiljb009"
                    class="animable"
                  ></path>
                  <path
                    d="M180.74,362.41a.48.48,0,0,1-.44-.28.49.49,0,0,1,.22-.67c9.26-4.69,23.95-22.23,24.1-22.41a.49.49,0,0,1,.7-.06.51.51,0,0,1,.06.71c-.6.72-15,17.87-24.41,22.65A.46.46,0,0,1,180.74,362.41Z"
                    style="
                      fill: rgb(64, 123, 255);
                      transform-origin: 192.87px 350.64px;
                    "
                    id="el8vkdt4vqht"
                    class="animable"
                  ></path>
                </g>
                <defs>
                  <filter id="active" height="200%">
                    <feMorphology
                      in="SourceAlpha"
                      result="DILATED"
                      operator="dilate"
                      radius="2"
                    ></feMorphology>
                    <feFlood
                      flood-color="#32DFEC"
                      flood-opacity="1"
                      result="PINK"
                    ></feFlood>
                    <feComposite
                      in="PINK"
                      in2="DILATED"
                      operator="in"
                      result="OUTLINE"
                    ></feComposite>
                    <feMerge>
                      <feMergeNode in="OUTLINE"></feMergeNode>
                      <feMergeNode in="SourceGraphic"></feMergeNode>
                    </feMerge>
                  </filter>
                  <filter id="hover" height="200%">
                    <feMorphology
                      in="SourceAlpha"
                      result="DILATED"
                      operator="dilate"
                      radius="2"
                    ></feMorphology>
                    <feFlood
                      flood-color="#ff0000"
                      flood-opacity="0.5"
                      result="PINK"
                    ></feFlood>
                    <feComposite
                      in="PINK"
                      in2="DILATED"
                      operator="in"
                      result="OUTLINE"
                    ></feComposite>
                    <feMerge>
                      <feMergeNode in="OUTLINE"></feMergeNode>
                      <feMergeNode in="SourceGraphic"></feMergeNode>
                    </feMerge>
                    <feColorMatrix
                      type="matrix"
                      values="0   0   0   0   0                0   1   0   0   0                0   0   0   0   0                0   0   0   1   0 "
                    ></feColorMatrix>
                  </filter>
                </defs>
              </svg>
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
