from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'topic1', # 토픽명
    bootstrap_servers=['kafka00:9092' ,'kafka01:9092', 'kafka02:9092'], # 카프카 브로커 주소 리스트
    auto_offset_reset='earliest', # 오프셋 위치(earliest:가장 처음, latest: 가장 최근)
    enable_auto_commit=True, # 오프셋 자동 커밋 여부
    group_id='test-group', # 컨슈머 그룹 식별자
    value_deserializer=lambda x: loads(x.decode('utf-8')), # 메시지의 값 역직렬화
    consumer_timeout_ms=1000 # 데이터를 기다리는 최대 시간
)

print('[Start] get consumer')

for message in consumer:
    print(f'Topic : {message.topic}, Partition : {message.partition}, Offset : {message.offset}, Key : {message.key}, value : {message.value}')

print('[End] get consumer')