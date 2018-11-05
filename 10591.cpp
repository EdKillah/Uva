#include <bits/stdc++.h>
#include <string>
#include <math.h>


using namespace std;

int main(){
	int num,n,final,x2=0,cases=1,suma=0;
	cin>>num;
	for(int i=0;i<num;i++){
		cin>>n;
		final = n;
		std::string aux = std::to_string(n);
		//char *intStr = itoa(n);
		//string aux = string(intStr);
		int x2=0;
		if(n>=10){
			//cout<<"ENTRA EN 13"<<endl;
			//cout<<"esto es aux   "<<aux<<endl;
			//cout<<"esta es su len "<<aux.length()<<endl;
			for (int j=0;j<aux.length();j++){
				//cout<<"n%10 "<<n%10<<endl;
				//cout<<"This is pow "<<pow((n%10),2)<<endl;
				//cout<<"X2 "<<x2<<endl;
				x2= x2+pow((n%10),2);
				//cout<<"checa x2 "<<x2<<endl;
				n = n/10;
				//cout<<"asi queda n "<<n<<endl;
				
			}
			//cout<<"XXXXXX2"<<x2<<endl;
		}
		
		else{
			x2 = pow(n,2);
		}
		bool band = true;
		while(band){
			aux = to_string(x2);
			suma = x2;
			x2 =0;
			for (int j=0;j<aux.length();j++){
				x2+=pow(suma%10,2);
				suma=suma/10;
			}
			if(x2<10){
				band=false;
				break;
			}
		}
		if(x2==1){
			cout<<"Case #"<<cases<<":"<<" "<<final<<" is a Happy number."<<endl;
		}
		else{
			cout<<"Case #"<<cases<<":"<<" "<<final<<" is an Unhappy number."<<endl;
		}
		cases++;
	}
	
	
	
	
	return 0;
}
