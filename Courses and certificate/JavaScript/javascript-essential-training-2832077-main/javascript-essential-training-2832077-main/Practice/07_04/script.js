/**
 * Cretae an array with several items
 * Remove the last item
 * Move the last item to the first position
 * Sort the items alphabetically
 * find a specific item in the array
 * Remove an item with specific content from the array (you can use nested methods or assign it to a variable)
 *
 */
//Creating an array
const arVar = [
  "laptop",
  "phone",
  "tv",
  "vape",
  "playStation",
  "blanket",
  "cable",
  "flower",
];

console.log(arVar);

// removing the last item
// arVar.splice(-1);

arVar.pop();

console.log(arVar);

//Move the last item to the first position
arVar.unshift(arVar.pop());
// cable item should be in the first position
console.log(arVar);

// Sort the items alphabetically
const sortedArr = arVar.sort();
//arVar.reverse() // Reverse the order
// blanket , cable , laptop, phone, playStation, tv, vape
console.log(sortedArr);

// find a specific item in the array
// const targetItem = arVar.find(item => item === "vape");
//    console.log(targetItem);

const targetItem = arVar.indexOf("vape");
const item = arVar[targetItem];
console.log(item);

// Remove an item with specific content from the array
// const index = arVar.indexOf("tv");
// arVar.splice(index, 1)
// console.log(arVar);

arVar.splice(arVar.indexOf("tv"), 1);
console.log(arVar);
