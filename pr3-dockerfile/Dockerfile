# использовать образ alpine как базовый
FROM alpine
# установить apache2
RUN apk update && apk add \
apache2 \
apache2-ctl
# указать порт, через который к сервисам можно обращаться внутри контейнера
EXPOSE 80
# скопировать файл index.html в директорию, из которой его возьмёт Apache
ADD ./index.html /var/www/localhost/htdocs/
# запустить apache2 в приоритетном режиме
CMD ["/usr/sbin/apachectl","-D", "FOREGROUND"]
