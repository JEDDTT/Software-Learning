/**
 * Practice: Making methods
 *
 * - Create a method for each object property.
 * - The method receives a value to match the property to be changed.
 * - Create a simple function to replace the current property value with the received value.
 * - Test the method by sending new values and checking the properties in the console.
 */

const backpack = {
  name: "Everyday Backpack",
  volume: 30,
  color: "grey",
  pocketNum: 15,
  strapLength: {
    left: 26,
    right: 26,
  },
  toggleLid: function (lidStatus) {
    this.lidOpen = lidStatus;
  },
  newStrapLength: function (lengthLeft, lengthRight) {
    this.strapLength.left = lengthLeft;
    this.strapLength.right = lengthRight;
  },
  newName: function (fname) {
    this.name = fname;
  },
  newColor: function (fColor) {
    this.color = fColor;
  },
  newVolume: function (fVolume) {
    this.volume = fVolume;
  },
  newPocketNum: function (fPocketNum) {
    this.pocketNum = fPocketNum;
  },
};
console.log(backpack.name);
backpack.newName("New Backpack");
console.log(backpack.name);
console.log(backpack.color);
backpack.newColor("Blue");
console.log(backpack.color);
console.log(backpack.pocketNum);
backpack.newPocketNum(10);
console.log(backpack.pocketNum);
