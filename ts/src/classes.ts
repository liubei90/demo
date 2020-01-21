function demoBasicClass() {
  class Greeter {
    greeting: string;
    constructor(greeting: string) {
      this.greeting = greeting;
    }
    greeter() {
      console.log(`hello, ${this.greeting}`);
    }
  }

  let g:Greeter = new Greeter('world');
  g.greeter();
}

function demoInheritanceClass() {
  class Animal {
    move(distance: number = 0) {
      console.log('animal move ' + distance);
    }
  }

  class Dog extends Animal {
    move(distance: number = 0) {
      console.log('dog move ' + distance);
    }
    bark() {
      console.log('Woof!');
    }
  }

  let d: Dog = new Dog();
  d.bark();
  d.move(5);
}

function demoAccessFieldClassAndReadonlyClass() {
  class Animal {
    private name: string;
    readonly numberOfLegs: number = 4;
    constructor(name: string) {
      this.name = name;
    }
  }

  let a: Animal = new Animal('dog');
  console.log(a.name);
  a.numberOfLegs = 2;
  console.log(a.numberOfLegs);
}

function demoParameterPropertiesClass() {
  class Animal {
    constructor(private name: string, readonly numberOfLegs: number = 4) {
    }
  }

  let a: Animal = new Animal('dog');
  console.log(a.name);
  console.log(a.numberOfLegs);
}

function demoAccessorsClass() {
  class Animal {
    constructor(private _name: string) {
      ;
    }
    get name():string {
      return this._name;
    }
    set name(v:string) {
      this._name = v;
    }
  }

  let a: Animal = new Animal('初一');
  console.log(a.name);
  a.name = '十五';
  console.log(a.name);
}

function demoStaticClass() {
  class Animal {
    static numberOfLeg: number = 4;
    bark() {
      console.log('animal number if leg is ' + Animal.numberOfLeg);
    }
  }

  let a: Animal = new Animal();
  a.bark();
}

function demoAbstractClass() {
  abstract class Animal {
    abstract bark(word: string): void;
  }

  class Dog extends Animal {
    bark(word: string) {
      console.log('Woof!, ' + word);
    }
  }

  let d: Dog = new Dog();
  d.bark('hahha');
}

function demo() {
  demoBasicClass();
  demoInheritanceClass();
  demoAccessFieldClassAndReadonlyClass();
  demoParameterPropertiesClass();
  demoAccessorsClass();
  demoStaticClass();
  demoAbstractClass();
}

export = demo;