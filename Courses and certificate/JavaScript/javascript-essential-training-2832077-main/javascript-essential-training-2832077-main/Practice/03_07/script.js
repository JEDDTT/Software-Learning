/**
 * Practice: Building objects
 *
 * - Create JavaScript objects based on objects in your current environment.
 * - Give each object an identifiable name.
 * - Create properties to describe the objects and set their values.
 * - Find an object that has another object inside of it to create a nested object.
 * - Test your objects in the browser console by accessing the entire object and its specific properties.
 */
const car = {
  brand: "Audi",
  model: "A4",
  year: 2014,
  fuel: "Petrol",
  type: "sedan",
};
const tv = {
  brand: "Hsense",
  model: "Hisense Smart TV",
  year: 2020,
  type: "Smart TV",
  inch: 50,
};

const pc = {
  brand: "HP",
  model: "HP Notebook",
  year: 2020,
  type: "Notebook",
  feature: {
    memory_rom: "500gb",
    memory_ram: "16gb",
    disk_type: "ssd",
    processor: "I5 9th Generation",
  },
};
