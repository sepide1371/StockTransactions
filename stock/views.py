import csv
import os

from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.decorators import action

import stock.serialaizers as serial
import stock.webservices as ws
from StockTransactions.utils import CustomResponse


class GetTradeInfo(APIView):
    @swagger_auto_schema(methods=['post'], request_body=serial.TradeInfoSerializer)
    @action(detail=False, methods=['post'])
    def post(self, request):
        selected_date = request.data
        serializer = serial.TradeInfoSerializer(data=selected_date)
        serializer.is_valid(raise_exception=True)
        valid_input = serializer.validated_data
        res = ws.trade_info(valid_input.get("date"))
        if res['tradeHistory']:
            serializer_output = serial.GetStockInfoOutputSerializer(res['tradeHistory'], many=True, read_only=True)
            csv_header = ['hEven', 'pTran', 'qTitTran']
            file_name = str(valid_input.get("date")) + '-trade.csv'
            with open(file_name, 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(csv_header)
                for item in serializer_output.data:
                    print(item)
                    data = [item["hEven"], item["pTran"], item["qTitTran"]]
                    writer.writerow(data)
            msg = {
                "message": "the information was successfully saved in {}".format(file_name)
            }
            return CustomResponse(msg, 0, msg_status=0)
        msg = {
            "message": "no information found for {}".format(valid_input.get("date"))
        }
        return CustomResponse(msg, 3, msg_status=0)


class TradeInfo(APIView):
    @swagger_auto_schema(methods=['post'], request_body=serial.TradeInfoSerializer)
    @action(detail=False, methods=['post'])
    def post(self, request):
        selected_date = request.data
        serializer = serial.TradeInfoSerializer(data=selected_date)
        serializer.is_valid(raise_exception=True)
        valid_input = serializer.validated_data
        file_name = str(valid_input.get("date")) + '-trade.csv'
        try:
            file = open(file_name)
        except:
            msg = {
                    "message": "file not found for {}".format(valid_input.get("date"))
                }
            return CustomResponse(msg, 3, msg_status=0)

        reader = csv.reader(file)
        lines = len(list(reader))-1
        with open(file_name, 'r') as f:
            next(f)
            total_p = 0
            total_q = 0
            for row in csv.reader(f):
                try:
                    p_value = float(row[1])
                except ValueError:
                    p_value = 0
                try:
                    q_value = int(row[2])
                except ValueError:
                    q_value = 0
                total_p += p_value
                total_q += q_value
            print('The pTrad total is {}'.format(total_p))
            print('The qTitTrad total is {}'.format(total_q))
        avg_p = total_p/lines
        avg_q = total_q/lines
        msg = {
            "num_items": lines,
            "pTranSUM": total_p,
            "pTranAVG": avg_p,
            "qTitTranSUM": total_q,
            "qTitTranAVG": avg_q,
        }
        return CustomResponse(msg, 0, msg_status=0)
