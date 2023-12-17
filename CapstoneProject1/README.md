


> docker build -t ml .

> docker run -it --rm -p 9696:9696 ml

> python predict_test.py
expected class: ALL {'all': '0.9530534744262695', 'hem': '0.046946526'}
expected class: HEM {'all': '0.20552486181259155', 'hem': '0.79447514'}



