# 핵심

![핵심](Django.assets/핵심.JPG)

우리가 앞으로 배울 것은 결국 누구에게 무엇을 요청하여 브라우저를 받아 올 것인가 이다. 



# Framework 이해하기 

누군가 만들어 놓은 코드를 재사용 하는 것

=> 반복되는 패턴은 오픈 소스를 가져 와서 빠르게 처리하기 위한 도구

가장 인기 많은 프레임워크



# Static web & Dynamic Web

Static web: 누가 보더라도 보여지는 정보가 같다. 

Dynamic web: 사용자에 따라 정보가 다르게 보인다. (네이버 메인의 날씨 정보, 로그인 정보등)

# 문서정리

인터넷: 인터넷은 모든 컴퓨터를 연결하고 어떤 일이 있어도 연결 상태를 유지할 수있는 방법을 찾는 방법입니다.

인터넷은 컴퓨터 간의 연결이다. 

라우터는 컴퓨터가 각각 연결을 하려면 너무 많은 연결이 필요하니까 이걸 컴퓨터 connect 라우터, 라우터 connect 컴퓨터의 방법으로 연결을 하여 컴퓨터와 라우터 한개의 연결만 있으면 다른 모든 컴퓨터와 연결이 가능하게 하였다. 

모뎀은 컴퓨터 정보를 전화정보로 바꿀 수 있고 반대가 가능한 장비이다. 이것을 통하여 기존에 깔려 있던 전화선을 통하여 컴퓨터간의 교류를 할 수 있게 해 주었다. 

TCP/IP: 전송 제어 규약, 인터넷 규약. 데이터가 어떻게 웹을 건너가는지 정의. 차 또는 자전거, 두 다리와 같은 역할을 한다. 

HTTP: 하이퍼텍스트 전송 규약. 클라이언트와 서버가 서로 통신할 수 있는 언어 정의. 주문할때 한국어 쓸지, 영어 쓸지와 같음. 

클라이언트: 오직 클라이언트만 HTTP 요청을 만들 수 있다. 그리고 반드시 URL(웹 주소) 파일들을 제공해야 한다.  웹 서버는 반드시 모든 HTTP 요청에 응답해야한다.

서버: 요청받은 URL이 존재하는 파일과 매칭되는지 확인, 해당 파일 돌려주거나, 필요한 파일 구축.

없으면 에러메시지 반환.

DNS: 도메인 이름 시스템. 주소록과 같음. 상점 주소 찾는거와 같음.

정적인 페이지는 난이도가 작고

동적인 페이지는 서버가 컨텐츠를 처리해야 하고 데이터베이스로부터 생성을 해야한다. 그래서 난이도가 높다. 

그러니까 정적인 페이지는 필요할 때 한번 요청하고 끝인데. 동적인 페이지는 계속 연결이 되어 있어야 하고 이 차이로 엄천난 트레픽 차이가 존재한다. 

# 서버 기초 

## IP와 도메인은 무엇일까요

IP주소는 일종의 id와 같다. 이 수많은 컴퓨터가 연결이 되고 컴퓨터는 서로를 구분을 지어야 했고 이때 각각에 id를 부여 했는데 그것이 IP주소 이다. 

도메인은 IP주소는 숫자로 구성이 되어 있으니까 사람이 한눈에 알아보기가 어려워 사람이 기억하기 편하게 문자로 바꾸어 놓은 것을 말한다.

client-side code: 프론트 엔드

Server-side code: 백엔드

## 클라이언트와 서버는 무엇일까요?

클라이언트와 서버 

소비자와 서비스제공업체와의 관계

클라이언트: 인터넷에 연결된 장치들이 이용 가능한 웹에 접근하는 소프트웨어(크롬, 파이어 폭스)

서버: 웹페이지, 사이트, 앱을 저장하는 컴퓨터. 클라이언트에서 요청을 보내면 사본을 보냅니다. 

그러니까 클라이언트는 HTTP를 사용하여 무슨 언어로 전달할지 선택하고, TCP/IP를 사용하여 데이터를 주고 받고, 간 데이터는 해당 서버에 내가 원하는 정보를 요청하고 서버는 그에 맞는 데이터 사본을 복사하여 사용자에게 보내준다. 



## 정적 웹 사이트와 동적 웹 사이트의 차이점은 무엇일까요? Django는 무엇을 위한 도구인가요?

정적 웹 사이트와 동적 웹 사이트는 애니메이션, 반응형 웹 이런 차이가 아니라 클라이언트가 정보를 요청을 할 때만 보내는가 혹인 날씨나 사용자 추천 알고리즘등 실시간 업데이트가 필요한다든가 유저가 서버로 부터 동영상등 지속적으로 정보를 교환해야 하는가에 의해 구분이 된다. 

그러니까 정적과 동적은 우리에게 보여지는 웹이 움지이냐 안 움직이느냐가 아니라 사용자 클릭등에 의한 요청에 의해서만 데이터가 바뀌는가 아니면 상황에 따라 필요한 정보를 자동으로 요청하는가에 의해 결정이 된다. 

동적 웹 사이트 추가 설명: 사용자 또는 저장된 환경을 기반으로 URL에 대해 다른 데이터를 반환 할 수 있고, 응답하는 과정에서 다른 작업을 수행 할 수 있다. 

그리고 이 지원하는 코드는 서버에서 실행을 되어야 하는데 이러한 코드를 만드는 것을 back-end라고 한다. (PHP, Python, Ruby 그리고 C#등 다양한 언어로 가능)

정적 웹 사이트: mdn

동적 웹 사이트: 네이버 금융

Django는 무엇을 위한 도구인가요?: 프레인워크는 코드 구성 요소의 모음이고 이를 활용해 복잡한 코드를 빠르게 작성할 수 있습니다. 

### 서버측에서 할 수 있는것 

고객 선호도 및 이전 구매 습관을 기반으로 한 제품 제안, 구매 단순화 등

정보를 저장하고 권한이있는 사용자만 보고 거래 가능

#### 효율적인 저장소와 정보 전달

데이터베이스를 사용하면 이러한 정보를 효율적으로 저장하고 공유 할 수 있으며 정보의 표시를 한 곳에서만 제어 할 수 있습니다.

#### 맞춤형 사용자 경험

서버는 사용자에게 편안함과 맞춤형 사용자 경험을 제공하기 위해 사용자의 정보를 사용하거나 저장 할 수 있습니다.

#### 컨텐츠에 대한 접근 제한

ex)친구 만 보거나 댓글을 달 수 있는 기능

#### 세션과 상태 저장

서버가 현재 사이트의 사용자 정보를 저장하거나 정보에 기반한 다른 응답을 보낼 수 있는 기본적인 메커니즘 입니다.

ex)사이트 사용하면 상태를 저장하여 사용자가 사이트를 다시 이용할 때 떠났던 부분부터 다시 할 수 있습니다.

#### 알림과 대화

자동으로 보내지는 메시지

#### 정보분석

웹사이트는 사용자에대한 많은 정보를 수집할 수 있습니다: 그들이 뭘 검색하는지, 그들이 뭘 사는지, 그들이 뭘 추천하는지, 그들이 각 페이지 마다 얼마나 머무르는지. 서버 측 프로그래밍을 사용하여 데이터의 분석을 기반으로 응답을 구체화 할 수 있습니다.

## HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요?

HTTP는 html문서와 같은 리소스들을 가져 올 수 있도록 해 주는 규약이고, 모든 데어터의 교환의 기초이고, 클라이언트-서버 규약이기도 하다. 

구성요소는 

요청은 하나의 개체, 사용자 에이전트(대부분 브라우저)에 의해 전송되고

응답은 게이트웨이 또는 프록시 등이 있습니다. 

사용자 에이전트

사용자를 대신하여 동작하는 모든 도구이고 항상 요청을 보내는 개체.

웹서버

요청에 대한 문서를 제공하는 서버. 

서버는 반드시 단일 머신일 필요는 없지만, 여러 개의 서버를 동일한 머신 위에서 호스팅 할 수는 있습니다. HTTP/1.1과 [`Host`](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Host) 헤더를 이용하여, 동일한 IP 주소를 공유할 수도 있습니다.

프록시

[프록시](https://developer.mozilla.org/ko/docs/Web/HTTP/Overview)

웹 브라우저와 서버 사이에서는 수많은 컴퓨터와 머신이 HTTP 메시지를 이어 받고 전달합니다. HTTP 계층에서는 이들이 어떻게 동작하는지 눈에 보이지 않습니다.이러한 컴퓨터/머신 중에서도 애플리케이션 계층에서 동작하는 것들을 일반적으로 **프록시**라고 부릅니다.

- 캐싱 (캐시는 공개 또는 비공개가 될 수 있습니다 (예: 브라우저 캐시))
- 필터링 (바이러스 백신 스캔, 유해 컨텐츠 차단(자녀 보호) 기능)
- 로드 밸런싱 (여러 서버들이 서로 다른 요청을 처리하도록 허용)
- 인증 (다양한 리소스에 대한 접근 제어)
- 로깅 (이력 정보를 저장)

으로 구성

### 요청

HTTP 요청의 예:

요청은 다음의 요소들로 구성됩니다:

- HTTP [메서드](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods), 보통 클라이언트가 수행하고자 하는 동작을 정의한 [`GET`](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/GET), [`POST`](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/POST) 같은 동사나 [`OPTIONS`](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/OPTIONS)나 [`HEAD`](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/HEAD)와 같은 명사입니다. 
  ```html
  <form action="" method="get" class="form-example"> 
  ```

  get, post 등 

- 가져오려는 리소스의 경로; 예를 들면 [프로토콜](https://developer.mozilla.org/ko/docs/Glossary/Protocol) (`http://`), [도메인 (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Domain) (여기서는 `developer.mozilla.org`), 또는 TCP [포트 (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Port) (여기서는 `80`)인 요소들을 제거한 리소스의 URL입니다.

- HTTP 프로토콜의 버전.(공통)

- 서버에 대한 추가 정보를 전달하는 선택적 [헤더들](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).(공통)

- `POST`와 같은 몇 가지 메서드를 위한, 전송된 리소스를 포함하는 응답의 본문과 유사한 본문.(전송)

### 응답

응답의 예:

응답은 다음의 요소들로 구성됩니다:

- HTTP 프로토콜의 버전.
- 요청의 성공 여부와, 그 이유를 나타내는 [상태 코드](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).(status code 200등)
- 아무런 영향력이 없는, 상태 코드의 짧은 설명을 나타내는 상태 메시지.(공통)
- 요청 헤더와 비슷한, HTTP [헤더들](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).(공통)
- 선택 사항으로, 가져온 리소스가 포함되는 본문.(받기)



#### HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요?(feat.김문경)

- HTTP : HyperText Transfer Protocol
- HTML과 같은 문서를 전송하기 위한 프로토콜(규칙)
- HTTP 메시지에는 요청과 응답 유형이 존재

[![HTTP_messages](https://camo.githubusercontent.com/14587a2fd82fcfc9b0c9636399c4c4a940e53b1f37a9783ca72f259ab0a07180/68747470733a2f2f69302e77702e636f6d2f68616e616d6f6e2e6b722f77702d636f6e74656e742f75706c6f6164732f323032312f30362f485454505f6d657373616765732e706e673f726573697a653d3832312532433234342673736c3d31)](https://camo.githubusercontent.com/14587a2fd82fcfc9b0c9636399c4c4a940e53b1f37a9783ca72f259ab0a07180/68747470733a2f2f69302e77702e636f6d2f68616e616d6f6e2e6b722f77702d636f6e74656e742f75706c6f6164732f323032312f30362f485454505f6d657373616765732e706e673f726573697a653d3832312532433234342673736c3d31)

> <기본 구조>
>
> 1. Start line : 요청이나 응답의 상태를 나타냄, 항상 첫번째 줄에 위치
> 2. HTTP headers : 요청을 지정하거나, 메시지에 포함된 본문을 설명하는 헤더의 집합
> 3. empty line : 헤더와 본문을 구분하는 빈 줄
> 4. body : 요청 / 응답과 관련된 데이터나 문서를 포함
>
> 참고 : [https://hanamon.kr/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-http-%EB%A9%94%EC%84%B8%EC%A7%80-message-%EC%9A%94%EC%B2%AD%EA%B3%BC-%EC%9D%91%EB%8B%B5-%EA%B5%AC%EC%A1%B0/](https://hanamon.kr/네트워크-http-메세지-message-요청과-응답-구조/)