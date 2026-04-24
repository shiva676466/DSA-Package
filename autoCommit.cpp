#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <unistd.h>

using namespace std;

int main() {
    ofstream file("daily_log.txt", ios::app);

    time_t now = time(0);
    file << "Commit made at: " << ctime(&now);
    file.close();

    system("git add .");
    system("git commit -m \"Daily auto commit\"");
    system("git push");

    cout << "Done\n";
    return 0;
}
