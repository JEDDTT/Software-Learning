/**
 * Practice: Pass values between functions
 *
 * - Create two functions
 * - Main function creates article element with data from object
 * - Helper function creates.
 * -Create a basic function declaration
 * -Make changes to elements in the DOM(querySelector, adding a class and so on...)
 * - Call the function declaration
 * - create basic function expression and repeat the previous steps of creating a basic function
 * - Create an arrow function
 */

const person = {
  name: "Emmanuel",
  Age: 28,
  race: "Black",
  weigth: "98 kg",
  heigth: "1m90",
};
const person2 = {
  name: "Daniel",
  Age: 25,
  race: "Black",
  weigth: "100 kg",
  heigth: "1m88",
};
function addperson(person) {
  const content = document.createElement("article");
  content.setAttribute("class", "articlePers");
  content.innerHTML = `
    <h1> ${person.name} </h1>
    <ul> 
    <li> Age: ${person.Age}</li>
    <li> Race: ${person.race}</li>
    <li> Weigth: ${person.weigth}</li>
    <li> Heigth: ${person.heigth}</li>
    </ul>
    `;
  return content;
}
const addperson2 = function (person2) {
  const content = document.createElement("article");
  content.setAttribute("class", "articlePers2");
  content.innerHTML = `
      <h1> ${person2.name} </h1>
      <ul> 
      <li> Age: ${person2.Age}</li>
      <li> Race: ${person2.race}</li>
      <li> Weigth: ${person2.weigth}</li>
      <li> Heigth: ${person2.heigth}</li>
      </ul>
      `;
  return content;
};

const addMessage = (message) => {
  const content = document.createElement("article");
  content.setAttribute("class", "articlePers2");
  content.innerHTML = `<p> <strong> ${message} </strong> </p>`;
  return content;
};
const main = document.querySelector("main");

main.append(addperson(person));
main.prepend(addperson2(person2));
main.append(addMessage("Objectives accomplished"));
