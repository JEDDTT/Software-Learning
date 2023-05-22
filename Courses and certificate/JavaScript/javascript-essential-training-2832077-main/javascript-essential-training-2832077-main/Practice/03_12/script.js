/**
 * Practice: Making classes and objects
 *
 * - Find a type of object you have more than one of in your house (eg. clothing, writing tools, etc).
 * - Create a class describing this object type - its properties and methods.
 * - Create several objects using the class.
 * - Test the objecs by calling their properties and using their methods in the console.
 */
import Backpack from "./Backpack.js";
import car from "./car.js";
import pc from "./pc.js";

const newCar = new car("BMW", "M3", 2020, "Diesel", "Sedan");

console.log(newCar);

const newBackpack = new Backpack(
  "myNewBackPack",
  30,
  "blue",
  15,
  10,
  10,
  false
);
console.log(newBackpack);

const newPC = new pc("Dell", 2019, "100gb", "8gb", "I5");
console.log(newPC);
