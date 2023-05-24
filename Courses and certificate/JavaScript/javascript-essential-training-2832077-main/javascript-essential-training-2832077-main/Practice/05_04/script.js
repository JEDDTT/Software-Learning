/**
 * Note: This file is intentionally empty.
 * You can use it to test your skills at traversing the DOM using JavaScript.
 */
/**   1. Identify specific elements you want to target
 *    2. Use the console or script.js to find those target elements
 *    3. Target specific elements nested inside other elements
 *    4. Try advanced CSS queries to get specific targets
 *    5. Experiment with querySelector and querySelectorAll
 *    6. Try populating a variable with an element higher up in the DOM, then use a querySelector
 *       on that variable to find one of its children
 */

/** 1-3
 */

document
  .querySelectorAll(".leftLength button")
  .forEach((item) => (item.style.backgroundColor = "red"));
document
  .querySelectorAll(".rightLength button")
  .forEach((item) => (item.style.backgroundColor = "red"));
/** Accessing the button for the right and left strap of the backpack */

// 4-5
document
  .querySelectorAll(".backpack__features li:last-child")
  .forEach((item) => (item.style.backgroundColor = "Blue"));

// 5-6
const backPackFeature = document.querySelector(".backpack__features");

console.log(backPackFeature);

const volume = backPackFeature.querySelector("li:first-child");
console.log(volume);
