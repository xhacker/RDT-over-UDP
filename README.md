# RDT Over UDP

## Interceptor
Usage: python interceptor.py FromSenderPort ToReceiverPort FromReceiverPort ToSenderPort
python interceptor.py 1600 1601 1602 1603

## Sender
python sender.py 127.0.0.1 1600 127.0.0.1 1603 "Open the pod bay doors"

## Receiver
python receiver.py 127.0.0.1 1602 127.0.0.1 1601
