class car {
  constructor(brand, model, color, year, fuel, type) {
    this.brand = brand;
    this.model = model;
    this.color = color;
    this.year = year;
    this.fuel = fuel;
    this.type = type;
  }

  changeBrand(newBrand) {
    this.brand = newBrand;
  }
  changeModel(newModel) {
    this.newModel = newModel;
  }
  changeColor(newColor) {
    this.color = newColor;
  }
}

export default car;
