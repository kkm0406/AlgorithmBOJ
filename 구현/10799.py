#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main()
{
    string s;
    cin>>s;
    int pipe = 0, cnt = 0;
    stack<char> st; 
    for(int i=0;i<s.length();i++){
        if(s[i] == '('){
            st.push('('); // 파이프 개수 추가
        }else{
            if(s[i-1] == '('){
                st.pop(); //이전이 바로 여는 괄호면 레이저
                cnt+=st.size(); //파이프 개수만큼 추가
            }else{
                cnt += 1; //맨 끝에 자투
                st.pop();
            }
        }
    }
    cout<<cnt;

    return 0;
}
