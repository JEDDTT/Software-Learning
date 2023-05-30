/**
 * Practice: Pass values between functions
 *
 * Create two functions:
 * - Main function
 *  - Creates new <article> element
 *  - Populates <article> with content (see const content below)
 *  - Returns <article> element to where function is called
 * - Helper image function
 *  - Creates new <figure> element
 *  - Adds <img> markup pointing to frogpack.image
 *  - Adds <figcaption> element with image description
 *  - Returns <figure> element to where function is called
 */

const frogpack = {
  name: "Frog Backpack",
  volume: 8,
  color: "green",
  pocketNum: 3,
  strapLength: {
    left: 10,
    right: 10,
  },
  lidOpen: false,
  image: "../../assets/images/frog.svg",
  toggleLid: function (lidStatus) {
    this.lidOpen = lidStatus;
  },
  newStrapLength: function (lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  },
};
const laptop = {
  manufacturer: "HP",
  model: "HP 14s",
  bios: "f.21",
  color: "Grey",
  processor: "I5-1135G7",
  memory: {
    rom: "500gb",
    ram: "16gb",
  },
  display: "Intel Iris",
  image: "images/HP-14s-feat.png",
  description: "A grey modern HP notebook, that is quite portable.",
  upgradedMemory: (ram, rom) => {
    this.memory.ram = ram;
    this.memory.rom = rom;
  },
};
// Baseline HTML output
const content = `
    <h1 class="laptop__model">${laptop.model}</h1>
    <ul class="laptop__features">
      <li class="laptop laptop__bios">BIOS:<span> ${laptop.bios}l</span></li>
      <li class="laptop laptop__color">Color:<span> ${laptop.color}</span></li>
      <li class="laptop laptop__processor">Processor:<span> ${laptop.processor}</span></li>
      <li class="laptop memory__rom">Memory ROM:<span> ${laptop.memory.rom}</span></li>
      <li class="laptop memory__ram">Memory RAM:<span> ${laptop.memory.ram}</span></li>
      <li class="laptop laptop__manufacturer">Manufacturer:<span> ${laptop.manufacturer}</span></li>
    </ul>  
`;

// Images function
const imageFunct = function (object) {
  let newFig = document.createElement("figure");
  let newImg = document.createElement("img");
  // adding attributes to the element
  newImg.setAttribute("src", object.image);
  newImg.setAttribute("alt", "HP laptop");
  newImg.style.display = "block";
  // creating a figcaption element and assign to the object's description
  let newDescription = document.createElement("figcaption");
  newDescription.innerHTML = object.description;
  // appending the img and figcaption the figure element and return the figure
  newFig.append(newImg, newDescription);
  return newFig;
};

// Main function. hence the content use the laptop data, we should the laptop object as a parameter
const mainFunct = (laptop) => {
  let newArticle = document.createElement("article");
  newArticle.innerHTML = content;
  newArticle.prepend(imageFunct(laptop));
  return newArticle;
};

const mainHTML = document.querySelector("main");
mainHTML.append(mainFunct(laptop));
