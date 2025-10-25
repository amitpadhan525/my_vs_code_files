#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <chrono>
#include <thread>
#include <mutex>
#include <sstream>
#include <random>

using namespace std;
using Clock = std::chrono::system_clock;
using TimePt = std::chrono::time_point<Clock>;

struct Member {
    string id;
    string ip;
    int port;
    string status; // ALIVE, DEAD, LEFT
    TimePt ts;
};

map<string, Member> membership;
mutex mtx;
string my_ip = "127.0.0.1";
int my_port = 0;
string my_id;
int incarnation = 1;

// ------------------------
string now_ms_str() {
    auto ms = chrono::duration_cast<chrono::milliseconds>(Clock::now().time_since_epoch()).count();
    return to_string(ms);
}

string member_to_text(const Member &m) {
    auto ms = chrono::duration_cast<chrono::milliseconds>(m.ts.time_since_epoch()).count();
    stringstream ss;
    ss << m.id << " | " << m.status << " | last update: " << ms;
    return ss.str();
}

// ------------------------
void print_members() {
    lock_guard<mutex> lk(mtx);
    cout << "Membership list (" << membership.size() << "):\n";
    for (auto &p : membership) {
        cout << " - " << member_to_text(p.second) << endl;
    }
}

void join_network(int introducer_port) {
    lock_guard<mutex> lk(mtx);
    Member me{my_id, my_ip, my_port, "ALIVE", Clock::now()};
    membership[my_id] = me;
    if (introducer_port == 0)
        cout << "[INTRODUCER] Started network at port " << my_port << endl;
    else
        cout << "[JOIN] Node " << my_id << " joined via introducer " << introducer_port << endl;
}

void gossip() {
    lock_guard<mutex> lk(mtx);
    cout << "[GOSSIP] Sharing membership info with peers..." << endl;
    for (auto &p : membership)
        cout << "   " << member_to_text(p.second) << endl;
}

void mark_dead(string id) {
    lock_guard<mutex> lk(mtx);
    if (membership.count(id)) {
        membership[id].status = "DEAD";
        membership[id].ts = Clock::now();
        cout << "[DEAD] " << id << " marked as DEAD." << endl;
    } else {
        cout << "[WARN] No such member " << id << endl;
    }
}

void leave_network() {
    lock_guard<mutex> lk(mtx);
    membership[my_id].status = "LEFT";
    membership[my_id].ts = Clock::now();
    cout << "[LEAVE] Node " << my_id << " leaving network.\n";
}

// ------------------------
int main() {
    cout << "Enter your port number: ";
    cin >> my_port;

    cout << "Enter introducer port (0 if none): ";
    int introducer_port;
    cin >> introducer_port;

    my_id = my_ip + ":" + to_string(my_port);
    join_network(introducer_port);

    cout << "\nStarted node " << my_id << ". Type commands:\n";
    cout << " help | members | gossip | dead <id> | leave\n";

    string cmd;
    while (true) {
        cout << "> ";
        if (!(cin >> cmd)) break;
        if (cmd == "members") print_members();
        else if (cmd == "gossip") gossip();
        else if (cmd == "dead") {
            string id;
            cin >> id;
            mark_dead(id);
        }
        else if (cmd == "leave") {
            leave_network();
            break;
        }
        else if (cmd == "help") {
            cout << "Commands:\n members - show membership\n gossip - simulate gossip\n dead <id> - mark node as dead\n leave - exit network\n";
        }
        else cout << "Unknown command. Type 'help'.\n";
    }

    
    cout << "Exited.\n";
    return 0;
}