//
//  main.cpp
//  project 7
//
//  Created by Kathryn Dullerud on 8/6/19.
//  Copyright © 2019 Kathryn Dullerud. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <vector>

using namespace std;

/// Here's the Robot class definition
class Robot
{
public:
    Robot(){feet=0, legs=0, arms=0, hands=0, torso=0, head=0, antenna=0, laser=0;}
    void print();
    bool addFeet();
    bool addLeg();
    bool addArm();
    bool addHand();
    bool addTorso();
    bool addHead();
    bool addAntenna();
    bool addLaser();
    int countFeet(){return feet;}
    int countLegs(){return legs;}
    int countArms(){return arms;}
    int countHands(){return hands;}
    int countTorso(){return torso;}
    int countHead(){return head;}
    int countAntennae(){return antenna;}
    int countLaser(){return laser;}
    bool complete();
    void setName(string n){getline(cin,n); name=n;};
    string getName(){return name;}
private:
    int feet;
    int legs;
    int arms;
    int hands;
    int torso;
    int head;
    int antenna;
    int laser;
    string name;
};

/// Here's the code associated with Robot
bool Robot::addFeet(){
    if (feet<2){
        feet++;
        return true;
    }
    else
        return false;
}
bool Robot::addLeg(){
    if (legs<feet && legs<2){
        legs++;
        return true;
    }
    else
        return false;
}
bool Robot::addTorso(){
    if (legs==2 && torso<1){
        torso++;
        return true;
    }
    else
        return false;
}

bool Robot::addArm(){
    if (torso==1 && arms<2){
        arms++;
        return true;
    }
    else
        return false;
}

bool Robot::addHand(){
    if (arms>hands && hands<2){
        hands++;
        return true;
    }
    else
        return false;
}

bool Robot::addHead(){
    if (torso==1 && head==0){
        head++;
        return true;
    }
    else
        return false;
}

bool Robot::addAntenna(){
    if (head==1 && antenna==0){
        antenna++;
        return true;
    }
    else
        return false;
}

bool Robot::addLaser(){
    if (hands>0 && laser==0){
        laser++;
        return true;
    }
    else
        return false;
}

bool Robot::complete(){
    bool completion;
    if (countFeet()==2 && countLegs()==2 && countTorso()==1 && countArms()==2 && countHead()==1 && countHands()==2 && countAntennae()==1 && countLaser()==1)
        completion=true;
    else
        completion=false;
    return completion;
}

void Robot::print()
{
    cout << "Robot: ";
    cout << "Number of feet: " << countFeet() << " Number of legs: " << countLegs() << " Number of torsos: " << countTorso();
    cout << " Number of arms: " << countArms() << " Number of hands: " << countHands() << " Number of heads: " << countHead();
    cout << " Number of antennae: " << countAntennae() << " Number of lasers: " << countLaser();
    cout << endl;
}

/// Here's the game controller class
class RobotController
{
public:
    void initializeGame(int numPlayers);
    void playGame();
private:
    vector<Robot> m_Robots;
};

void RobotController::initializeGame(int numPlayers){
    m_Robots.resize(0);
    m_Robots.reserve(15);
    m_Robots.resize(numPlayers);
    string player;
    for (int i=0; i<numPlayers; i++){
        cout << "Enter name of player: ";
        m_Robots[i].setName(player);
    }
}
void RobotController::playGame(){
    do {
        string input;
        string enter;
        cout << "Enter name of player whose turn it is: ";
        getline (cin,input);
        int n, diceRoll;
        for (int i=0; i<m_Robots.size(); i++){
            if (input==m_Robots[i].getName())
                n=i;
        }
        cout << "Enter a 0 to roll the die. ";
        getline (cin,enter);
        if (enter=="0"){
            diceRoll=rand() % 8 + 1;
            if (diceRoll==1)
                m_Robots[n].addFeet();
            if (diceRoll==2)
                m_Robots[n].addLeg();
            if (diceRoll==3)
                m_Robots[n].addTorso();
            if (diceRoll==4)
                m_Robots[n].addArm();
            if (diceRoll==5)
                m_Robots[n].addHand();
            if (diceRoll==6)
                m_Robots[n].addHead();
            if (diceRoll==7)
                m_Robots[n].addAntenna();
            if (diceRoll==8)
                m_Robots[n].addLaser();
            cout << "Roll: " << diceRoll << " Player: " << m_Robots[n].getName() << " ";
            m_Robots[n].print();
        }
    }
    while (m_Robots[0].complete()==false && m_Robots[1].complete()==false && m_Robots[2].complete()==false && m_Robots[3].complete()==false && m_Robots[4].complete()==false && m_Robots[5].complete()==false && m_Robots[6].complete()==false && m_Robots[7].complete()==false && m_Robots[8].complete()==false && m_Robots[9].complete()==false);
    for (int i=0; i<m_Robots.size(); i++)
        if (m_Robots[i].complete()==true)
            cout << m_Robots[i].getName() << " is the winner!";
}

int main(){
    string inputBuffer;
    int numberOfPlayers;
    RobotController gameManager;
    srand(time(0));
    do
    {
        cout << "How many players: ";
        getline(cin, inputBuffer);
        numberOfPlayers = atoi( inputBuffer.c_str() );
    }
    while (numberOfPlayers < 1 || numberOfPlayers > 9);
    do
    {
        gameManager.initializeGame(numberOfPlayers);
        gameManager.playGame();
        cout << endl << "Play Again? [y/n] ";
        getline(cin, inputBuffer);
    }
    while ( tolower(inputBuffer[0]) != 'n' );
    
    return 0;
}
