package org.example;

import java.time.ZonedDateTime;
import java.util.LinkedList;

public class MyLinkedList<SpaceMarines> extends LinkedList<SpaceMarine> {
    private final java.time.ZonedDateTime creationDate;
    MyLinkedList(){
        super();
        this.creationDate = ZonedDateTime.now();
    }
    public java.time.ZonedDateTime getCreationDate(){
        return creationDate;
    }
    public String getType(){
        return "java.util.LinkedList<org.example.SpaceMarine>";
    }
}
