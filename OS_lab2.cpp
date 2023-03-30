#include <stdio.h>
#include <queue>

using namespace std;

void print(){
    
}
int main(){

    int n = 0;
    scanf("%d", &n);
    int SA = 1;
    scanf("%d",&SA);
    int q = 0;
    if(SA == 2){
        scanf("%d",&q);
    }
    int RB[100][5];
    for(int i = 0; i < n; i++)
    {
        scanf("%d",&RB[i][0]);
        scanf("%d",&RB[i][1]);
        scanf("%d",&RB[i][2]);
        scanf("%d",&RB[i][3]);
        
        //the extra finishing one
        RB[i][4] = 1;
    }
    int running_time[100] = {};
    int stage[100] = {};
    bool terminate[100] = {};
    bool blocked[100] = {};
    queue<int> readylist;
    for(int i = 0; i < n; i++){
        readylist.push(i);
    }
    if(SA == 1){

        running_time[0] += 1;
        stage[0] = 0;
        int rp = 0;
        readylist.pop();
        printf("%10d     ",1);
        for(int j = 0; j < n; j++){
            if(blocked[j]){
                printf("blocked %3d of %3d;  ", running_time[j], RB[j][stage[j]]);
            } else if(terminate[j]){
                printf("done          ;  ");
            } else if(j == rp){
                if(stage[j] != 4){
                    printf("running %3d of %3d;  ", running_time[j], RB[j][stage[j]]);
                } else {
                    printf("terminating       ;  ");
                }
            } else {
                printf("ready             ;  ");
            }
        }
        printf("\n");
        for(int i = 2; ;i++){

            //printf("%d;%d;%d;%d;", readylist.size(),readylist.front(),rp,stage[rp]);

            //check if everything is done
            int flag = 1;
            for(int j = 0; j < n; j++){
                if(terminate[j] == 0)
                    flag = 0;
            }
            if(flag){
                break;
            }

            //decide running this process or find new process
            if(rp != -1 && running_time[rp] + 1 > RB[rp][stage[rp]]){
                
                //stop running this process
                if(stage[rp] == 4){
                    terminate[rp] = 1;
                    stage[rp] += 1;
                }
                else{
                    blocked[rp] = 1;
                    stage[rp] += 1;
                    running_time[rp] = 0;
                }
                rp = -1;

            }

            //taking care of block processes
            for(int j = 0; j < n; j++){
                if(blocked[j]){
                    //if blocking is finished
                    if(running_time[j]+1 > RB[j][stage[j]]){
                        stage[j] += 1;
                        running_time[j] = 0;
                        blocked[j] = 0;
                        readylist.push(j);
                    }else {
                        running_time[j] += 1;
                    }
                }
            }

            //find new process to run if not running
            if(rp == -1 && !readylist.empty()){
                rp = readylist.front();
                readylist.pop();
            }

            //running the process, whether it's the original one or not
            if(rp != -1){
                running_time[rp] += 1;
            }
            
            //check if everything is done
            flag = 1;
            for(int j = 0; j < n; j++){
                if(terminate[j] == 0)
                    flag = 0;
            }
            if(flag){
                break;
            }

            //printing them all
            printf("%10d     ",i);
            for(int j = 0; j < n; j++){
                if(blocked[j]){
                    printf("blocked %3d of %3d;  ", running_time[j], RB[j][stage[j]]);
                } else if(terminate[j]){
                    printf("done              ;  ");
                } else if(j == rp){
                    if(stage[j] != 4){
                        printf("running %3d of %3d;  ", running_time[j], RB[j][stage[j]]);
                    } else {
                        printf("terminating       ;  ");
                    }
                } else {
                    printf("ready             ;  ");
                }
            }
            //printf("%d;%d;%d;%d;", readylist.size(),readylist.front(),rp,stage[rp]);
            printf("\n");
        }
    }
    if(SA == 2){

        int rr = 1;
        running_time[0] += 1;
        stage[0] = 0;
        int rp = 0;
        readylist.pop();
        printf("%10d     ",1);
        for(int j = 0; j < n; j++){
            if(blocked[j]){
                printf("blocked %3d of %3d;  ", running_time[j], RB[j][stage[j]]);
            } else if(terminate[j]){
                printf("done          ;  ");
            } else if(j == rp){
                if(stage[j] != 4){
                    printf("running %3d of %3d;  ", running_time[j], RB[j][stage[j]]);
                } else {
                    printf("terminating       ;  ");
                }
            } else {
                printf("ready             ;  ");
            }
        }
        printf("\n");
        for(int i = 2; ;i++){

            //printf("%d;%d;%d;%d;", readylist.size(),readylist.front(),rp,stage[rp]);

            //check if everything is done
            int flag = 1;
            for(int j = 0; j < n; j++){
                if(terminate[j] == 0)
                    flag = 0;
            }
            if(flag){
                break;
            }

            //decide running this process or find new process
            if(rp != -1 && running_time[rp] + 1 > RB[rp][stage[rp]]){
                
                //stop running this process

                //if this process is finished; otherwise, blcok it
                if(stage[rp] == 4){
                    terminate[rp] = 1;
                    stage[rp] += 1;
                }
                else{
                    blocked[rp] = 1;
                    stage[rp] += 1;
                    running_time[rp] = 0;
                }
                rp = -1;
                rr = 0;
            }
            //if preemption is needed
            else if(rr + 1 > q){
                //stop running this process
                //must have remaining time left, push to ready list
                rr = 0;
                if(rp != -1)
                    readylist.push(rp);
                rp = -1;
            }

            //taking care of blocked processes
            for(int j = 0; j < n; j++){
                if(blocked[j]){
                    //if blocking is finished
                    if(running_time[j]+1 > RB[j][stage[j]]){
                        stage[j] += 1;
                        running_time[j] = 0;
                        blocked[j] = 0;
                        readylist.push(j);
                    }else {
                        running_time[j] += 1;
                    }
                }
            }

            //printf(" *** %d;%d;%d;%d;", readylist.size(),readylist.front(),rp,rr);
            //find new process to run if not running
            
            if(rp == -1 && !readylist.empty()){
                rp = readylist.front();
                readylist.pop();
            }

            //running the process, whether it's the original one or not
            if(rp != -1){
                running_time[rp] += 1;
                rr += 1;
            }else{
                rr = 0;
            }
            
            //check if everything is done
            flag = 1;
            for(int j = 0; j < n; j++){
                if(terminate[j] == 0)
                    flag = 0;
            }
            if(flag){
                break;
            }

            //printing them all
            printf("%10d     ",i);
            for(int j = 0; j < n; j++){
                if(blocked[j]){
                    printf("blocked %3d of %3d;  ", running_time[j], RB[j][stage[j]]);
                } else if(terminate[j]){
                    printf("done              ;  ");
                } else if(j == rp){
                    if(stage[j] != 4){
                        printf("running %3d of %3d;  ", running_time[j], RB[j][stage[j]]);
                    } else {
                        printf("terminating       ;  ");
                    }
                } else {
                    printf("ready             ;  ");
                }
            }
            //printf("%d;%d;%d;%d;", readylist.size(),readylist.front(),rp,stage[rp]);
            printf("\n");
        }


    }
}