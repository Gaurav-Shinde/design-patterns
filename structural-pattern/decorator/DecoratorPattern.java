/*
Decorator pattern: adds new behaviors to objects by placing them in wrapper objects with that behavior.
Hint: Think about Russian

Components:
- Interface component
- Wrapee class component that implement interface
- Decorator: Base asbtract Wrapper class that implements interface
- Decorator: Wrapper classes that extend base wrapper class
- client code

Uses:
- different notification systems

Example Explanation:
Notifier System
Imagine you have a food delivery app, which notifies users via email by default.
Your users ask to have other methods of notification, like sms, whatsapp.
So you create a interface for Notifier, and then just create implementations of it for each notification method.
Later, customers complain they want to recieve notifications through combination of notification methods.
Now this is a problem with current app design, as it will lead to make class implementations for each combination.
Not all languages allow multiple inheritance.
Inheritance create an object that inherits behaviors from parent.
Aggregation or Composition creates references to other objects to delegate work - add extra behavior at runtime.
Enter the decorator pattern, which relies on Object Composition over Inheritance. 
This will allow us to create wrappers instead that implement the Notifier interface.
Wrapper can send notification and call other notification methods as needed. 
This helps reuse the notification method with any combination of notification methods.

Output:
Begin to send notifications using NotificationComponent for admin in Food Delivery App...
Sending an email to admin@gmail.com ...
Message is:
Hello World!

Begin to send notifications using NotificationComponent for admin in Food Delivery App...
Sending an text to 1234567890 over Whatsapp ...
Message is:
Hello World!

Begin to send notifications using NotificationComponent for admin in Food Delivery App...
Sending message to admin-personal-channel channel over Slack ...
Message is:
Hello World!

Begin to send notifications using NotificationComponent for admin in Food Delivery App...
Sending an email to admin@gmail.com ...
Message is:
Hello World!
Sending an text to 1234567890 over Whatsapp ...
Message is:
Hello World!
Sending message to admin-personal-channel channel over Slack ...
Message is:
Hello World!
*/

import java.util.Map;
import java.util.HashMap;

class DecoratorPattern{
    public static void main(String args[]){
        DatabaseService dbService = new DatabaseService();
        String username = "admin";
        dbService.addUser(username);
        
        NotificationComponent notificationComponent = new NotificationComponent(dbService,username);
        
        // Email only
        EmailBaseNotificationDecorator emailNotifier= new EmailBaseNotificationDecorator(dbService,notificationComponent);
        
        emailNotifier.send("Hello World!");
        System.out.println();
        
        // Whatsapp only
        WhatsappNotificationDecorator whatsappNotifier = new WhatsappNotificationDecorator(dbService, notificationComponent);
        whatsappNotifier.send("Hello World!");
        System.out.println();
        
        // Slack only
        SlackNotificationDecorator slackChannelNotifier = new SlackNotificationDecorator(dbService, notificationComponent);
        slackChannelNotifier.send("Hello World!");
        System.out.println();
        
        // Email and Whatsapp
        EmailBaseNotificationDecorator emailNotifier2= new EmailBaseNotificationDecorator(dbService,notificationComponent);
        
        WhatsappNotificationDecorator whatsappNotifier2 = new WhatsappNotificationDecorator(dbService, emailNotifier2);
        
        SlackNotificationDecorator slackChannelNotifier2 = new SlackNotificationDecorator(dbService, whatsappNotifier2);
        
        slackChannelNotifier2.send("Hello World!");
        System.out.println();
    }
}
public class DatabaseService{
    Map<String,Map> usersProps = new HashMap<String,Map>();
     
    // default constructor
     
    public String getEmailFromUsername(String username){
        return this.usersProps.get(username).get("email").toString();
    }
    public String getNumberFromUsername(String username){
        return this.usersProps.get(username).get("number").toString();
    }
    public String getSlackChannelFromUsername(String username){
        return this.usersProps.get(username).get("slack").toString();
    }
    
    // adds user with dummy number and email 
    // in userProps map as database
    public void addUser(String username){
        Map<String,String> userProps = new HashMap<String,String>();
        userProps.put("number","1234567890");
        userProps.put("email",username+"@gmail.com");
        userProps.put("slack",username+"-personal-channel");
    
        this.usersProps.put(username,userProps);
    }
}
public interface NotificationInterface{
    public void send(String message);
    public String getUsername();
}
public class NotificationComponent implements NotificationInterface{
    private final String username;
    protected final DatabaseService dbService;
    
    // default constructor
    NotificationComponent(DatabaseService dbService, String username){
        this.dbService = dbService;
        this.username = username;
    }
    
    public void send(String message){
        System.out.println(String.format("Begin to send notifications using NotificationComponent for %s in Food Delivery App...",username));
    }
    
    public String getUsername(){
        return this.username;
    }
}
public class EmailBaseNotificationDecorator implements NotificationInterface{
    
    public NotificationInterface notificationComponent;
    public DatabaseService dbService;
    
    EmailBaseNotificationDecorator(DatabaseService dbService,NotificationInterface notificationComponent){
        this.notificationComponent = notificationComponent;
        this.dbService = dbService;
    }
    public void send(String message){
        // dummy, just initiates notification chain
        notificationComponent.send(message); 
        
        // custom logic
        System.out.println(String.format("Sending an email to %s ...",this.dbService.getEmailFromUsername(getUsername()) ));
        System.out.println(String.format("Message is:\n%s",message));
    }
    // target
    public String getUsername(){
        return notificationComponent.getUsername();
    }
}
public class WhatsappNotificationDecorator extends EmailBaseNotificationDecorator{
    
    WhatsappNotificationDecorator(DatabaseService dbService, NotificationInterface notificationComponent){
        super(dbService,notificationComponent);
        
    }   
    
    public void send(String message){
        this.notificationComponent.send(message);
        
         // custom logic
        System.out.println(String.format("Sending an text to %s over Whatsapp ...",this.dbService.getNumberFromUsername(getUsername()) ));
        System.out.println(String.format("Message is:\n%s",message));
    }
    
    public String getUsername(){
        return notificationComponent.getUsername();
    }
}
public class SlackNotificationDecorator extends EmailBaseNotificationDecorator{
     SlackNotificationDecorator(DatabaseService dbService, NotificationInterface notificationComponent){
        super(dbService,notificationComponent);
        
    }   
    
    public void send(String message){
        this.notificationComponent.send(message);
        
         // custom logic
        System.out.println(String.format("Sending message to %s channel over Slack ...",this.dbService.getSlackChannelFromUsername(getUsername()) ));
        System.out.println(String.format("Message is:\n%s",message));
    }
    
    public String getUsername(){
        return notificationComponent.getUsername();
    }   
}
