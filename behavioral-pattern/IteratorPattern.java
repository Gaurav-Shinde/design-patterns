/*
Iterator pattern: create object to iterate through a collection object despite implementation
- Iterator encapsulates traversal details and abstracts object representation.


Ex: for a tree graph data structure, can iterate over nodes in DFS, BFS, etc using specific iterator.

Components:
- client code
- collection interface
- concrete collection
- iterator interface
- concreate iterator

Example:
Imagine you have social media accounts. You create an interface for it and implementations for each platform like facebook, instagram, etc.
They might have several different fields for each object of account class.
We focus on the list of friends for a person's account. Which is saved as a simple ArrayList of String collection.
We then create an FriendsIterator interface with common methods and implement it for Facebook (note we can implement other platforms too, but redundant here).
The account instance can create a FriendsIterator object for it, referencing that specific user account, to iterate over the friends list.

Output:
true
Abby
Andrew
Abraham
null
false
*/

/*
Other platform account iterators for friends would be same on other social media account
Because it is only List object type

If adding more iterators say for iterating over custom class objects, can add to the SocialNetworkAccount interface and implement them
*/

import java.util.List;
import java.util.ArrayList;

// main class
class IteratorPattern{
    public static void main(String args[]){
        clientCode();
    }
    // client code
    public static void clientCode(){
        
        // fake friends
        List<String> myFriends = new ArrayList<String>();
        myFriends.add("Abby");
        myFriends.add("Andrew");
        myFriends.add("Abraham");
        
        // fake account
        String myUsername = "April";
        SocialNetworkAccount myAccount = new FacebookAccount(myUsername,myFriends);
        
        // create iterator
        FriendsIterator myFacebookFriendsIterator = myAccount.createFriendsIterator();
        
        // test iterator functions
        System.out.println(myFacebookFriendsIterator.hasNext());
        System.out.println(myFacebookFriendsIterator.getNext());
        System.out.println(myFacebookFriendsIterator.getNext());
        System.out.println(myFacebookFriendsIterator.getNext());
        System.out.println(myFacebookFriendsIterator.getNext());
        System.out.println(myFacebookFriendsIterator.hasNext());
    }
}



// social network platform interface
public interface SocialNetworkAccount{
    public FriendsIterator createFriendsIterator();
    public List<String> getFriendsList();
}
// facebook
public class FacebookAccount implements SocialNetworkAccount{

    private String username;
    public List<String> friends;
    
    FacebookAccount(String username, List<String> friends){
        this.username = username;
        this.friends = friends;
    }
    public FriendsIterator createFriendsIterator(){
        return new FacebookFriendsIterator(this);
    }
    public List<String> getFriendsList(){
        return this.friends;
    }
}

// friends iterator interface
public interface FriendsIterator{
    public boolean hasNext();
    public String getNext();
    public void reset();
}
// facebook friends iterator
public class FacebookFriendsIterator implements FriendsIterator{
    private int currentPointer;
    private SocialNetworkAccount account;
    private List<String> friends;
    
    FacebookFriendsIterator(SocialNetworkAccount account){
        this.currentPointer=0;
        this.account=account;
        this.friends=this.account.getFriendsList();
    }
    
    public boolean hasNext(){
        if(currentPointer < this.friends.size()) return true;
        return false;
    }
    
    public String getNext(){
        if(!hasNext()) return null;
        return this.friends.get(currentPointer++);
    }
    
    public void reset(){
        this.currentPointer=0;
    }
}


