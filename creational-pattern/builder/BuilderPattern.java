  /*
  Builder pattern - create an complex object with many configurations
  - result obj returned from builder obj

  Problems it solves: long constructor values for creating desired product object

  Components:
  - client code
  - builder interface
  - each product builder class
  - director for common builds abstraction
  
  Ex: 
  Car builder that has options to build common car types with similar properties.
  */

class BuilderPattern {
    public static void main(String[] args) {

        Builder builder = new CarBuilder();
        Car car1 = builder.id(1).make("lamborghini").model("aventador").engine("v8").color("red").build();
        System.out.println(car1.toString());
        
        Director director = new Director();
        Car car2 = director.makeBuggattiChiron(2,"blue");
        System.out.println(car2.toString());
        Car car3 = director.makeLamborghiniAventador(3,"green");
        System.out.println(car3.toString());
    }
}
public class Car{
    private int id;
    private String make;
    private String model;
    private String engine;
    private String color = "white"; // default
    
    // Protected access constructor for all fields
    protected Car(int id, String make, String model, String engine, String color){
        this.id=id;
        this.make=make;
        this.model=model;
        this.engine=engine;
        this.color=color;
    }
    public String toString(){
        return String.format("Car{id=%d,make=%s,model=%s,engine=%s,color=%s}",this.id,this.make,this.model,this.engine,this.color);
    }
}

public interface Builder{
    public Builder id(int id);
    public Builder make(String make);
    public Builder model(String model);
    public Builder engine(String engine);
    public Builder color(String color);
    public Car build();
    public void resetFields();
}

public class CarBuilder implements Builder{
    private int id;
    private String make;
    private String model;
    private String engine;
    private String color = "white";
    
    public Builder id(int id){
        this.id=id;
        return this;
    }
    public Builder make(String make){
        this.make=make;
        return this;
    } 
    public Builder model(String model){
        this.model=model;
        return this;
    }
    public Builder engine(String engine){
        this.engine=engine;
        return this;
    }
    public Builder color(String color){
        this.color=color;
        return this;
    }
    public void resetFields(){
        this.id=0;
        this.make="";
        this.model="";
        this.engine="";
        this.color="";
    }
    public Car build(){
        Car result = new Car(this.id, this.make, this.model, this.engine, this.color);
        resetFields();
        return result;
    }
}
public class Director{
    // buggati chiron
    public Car makeBuggattiChiron(int id, String color){
        Builder builder = new CarBuilder();
        Car result = builder.id(id).make("buggatti").model("chiron").engine("v12").color(color).build();
    
        return result;
    }
    // lamborghini aventador
    public Car makeLamborghiniAventador(int id, String color){
        Builder builder = new CarBuilder();
        Car result = builder.id(id).make("lamborghini").model("aventador").engine("v8").color(color).build();
        return result;
    }
    
}


