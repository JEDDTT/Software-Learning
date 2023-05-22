/**
 * Challenge: Create a new object type
 *
 * - Create a new object type "Book" using a class or an object constructor function.
 * - Add at least 5 book objects.
 */

import Backpack from "./Backpack.js";
import Book from "./Book.js";

const everydayPack = new Backpack(
  "Everyday Backpack",
  30,
  "grey",
  15,
  26,
  26,
  false,
  "December 5, 2018 15:00:00 PST"
);

console.log("The everydayPack object:", everydayPack);
console.log("The pocketNum value:", everydayPack.pocketNum);
console.log("Days since aquired:", everydayPack.backpackAge());

const newBook = new Book(
  "48 laws of power",
  "Robert Green",
  "Simon and Schuster",
  1998,
  "roman"
);
console.log(newBook);

const unshakable = new Book(
  "Unshakable",
  "Tony Robins",
  "Simon and Schuster",
  2007,
  "roman"
);
console.log(unshakable);

const newBook2 = new Book(
  "How to manage your money like a grown up",
  "Sam Beckbessinger",
  "jonathan Ball",
  2018,
  "roman"
);
console.log(newBook2);

const newBook3 = new Book("Paper Route", "Young Dolph", "PRE", 2021, "roman");
console.log(newBook3);

const newBook4 = new Book("Glockoma 2", "Key Glock", "PRE", 2023, "roman");
console.log(newBook4);
