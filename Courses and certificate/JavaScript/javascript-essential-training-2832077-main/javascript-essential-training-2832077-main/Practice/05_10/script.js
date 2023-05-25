/**
 * Traverse the DOM tree using querySelector() and querySelectorAll()
 * @link https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector
 * @link https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll
 */
/**
 * Create a new element for a nav menu
 * Add unordered list with five items ||Home, about, contact...
 * Add a new navigation menu to the DOM directly after the header
 * Write basic CSS for a horizontal menu|| use display: flex, or grid
 *
 */

import Backpack from "./Backpack.js";

const everydayPack = new Backpack(
  "Everyday Backpack",
  30,
  "grey",
  15,
  26,
  26,
  false,
  "December 5, 2018 15:00:00 PST",
  "images/everyday.svg"
);

const content = `
  
    <figure class="backpack__image">
      <img src=${everydayPack.image} alt="" />
    </figure>
    <h1 class="backpack__name">${everydayPack.name}</h1>
    <ul class="backpack__features">
      <li class="packprop backpack__volume">Volume:<span> ${
        everydayPack.volume
      }l</span></li>
      <li class="packprop backpack__color">Color:<span> ${
        everydayPack.color
      }</span></li>
      <li class="backpack__age">Age:<span> ${everydayPack.backpackAge()} days old</span></li>
      <li class="packprop backpack__pockets">Number of pockets:<span> ${
        everydayPack.pocketNum
      }</span></li>
      <li class="packprop backpack__strap">Left strap length:<span> ${
        everydayPack.strapLength.left
      } inches</span></li>
      <li class="packprop backpack__strap">Right strap length:<span> ${
        everydayPack.strapLength.right
      } inches</span></li>
      <li class="packprop backpack__lid">Lid status:<span> ${
        everydayPack.lidOpen
      }</span></li>
    </ul>
  
`;

const navContent = ` 
      <li><a class="active" href="#Home" > Home </a></li>
      <li><a href="#Blog"> Blog </a></li>
      <li><a href="#Account"> Account </a></li>
      <li><a href="#About"> About </a></li>
      <li><a href="#Contact"> Contact </a></li>
`;

const main = document.querySelector(".maincontent");
const header = document.querySelector(".siteheader");

const newArticle = document.createElement("article");
newArticle.classList.add("backpack");
newArticle.setAttribute("id", "everyday");
newArticle.innerHTML = content; // inserting the content within the html element

const mainNav = document.createElement("nav");
mainNav.classList.add("main-navigation");
mainNav.setAttribute("id", "mainNavId");
const newUl = document.createElement("ul");
newUl.classList.add("navList");
newUl.setAttribute("id", "navId");
newUl.innerHTML = navContent;
mainNav.append(newUl); // try to use also innerHTML later on to see if it works, but I believe it works.

header.prepend(mainNav);

main.append(newArticle);
