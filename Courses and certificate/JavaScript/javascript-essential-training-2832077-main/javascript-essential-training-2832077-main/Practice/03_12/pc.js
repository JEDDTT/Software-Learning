// class pc

class pc {
  constructor(brand, year, rom, ram, processor) {
    this.brand = brand;
    this.year = year;
    this.feature = {
      from: rom,
      fram: ram,
      fprocessor: processor,
    };
  }
  changeBrand(newBrand) {
    this.brand = newBrand;
  }
  changeFeature(newRom, newRam, newprocessor) {
    this.feature.from = newRom;
    this.feature.fram = newRam;
    this.feature.fprocessor = newprocessor;
  }
}

export default pc;
