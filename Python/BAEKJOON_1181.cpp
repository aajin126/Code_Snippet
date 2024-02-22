#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

// 각 단어를 저장할 문자배열 포인트 20,000개
char *s[20000];

// 2개의 문장을 비교히여 크고 작음을 판단할 함수
bool comp(char *s1, char *s2){
	return strcmp(s1, s2)<0;
}

void Result()
{
	int n;	
	char tmp[51];
	
	// 단어 갯수를 입력
	scanf("%d", &n);

	// n개의 단어를 
	for(int i=0;i<n;++i)
	{	
		// 입력받고
		scanf("%s", tmp);
		// 메모리를 동적 할당
		// ( 문장길이 + 2글자(단어갯수) + 1글자('\0'문자) 
		// 단어 1개당 최대 53 글자 할당 필요
		s[i] = new char[strlen(tmp)+3];
		sprintf(s[i], "%02d%s", strlen(tmp), tmp);
	}	

	// C++의 정렬 기능을 사용합니다.
	// s 부터 s+n 포인터 목록까지
	// comp 함수가 정렬판단 조건 함수가 됩니다.
	sort(s, s+n, comp);

	// 이제 단어 목록을 n개 출력하는데,
	for(int i=0;i<n;++i)
	{
		// 바로 앞에 출력했던 단어와 똑같다면 출력하지 않습니다.
		if(i>0 && strcmp(s[i-1], s[i])==0)continue;
		// 출력할 때는 앞의 2자리 숫자는 빼고 출력합니다.
		printf("%s\n", &s[i][2]);
	}
}

int main()
{
	Result();
	return 0;
}