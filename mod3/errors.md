# Ошибки в коде
## Ошибка в методе <i>get_age</i>

>   ## В этом методе некорректно считался возраст
>   ### Было
>     
>      def get_age(self):
>          now = datetime.datetime.now()
>          return self.yob-now.year 
>   ### Стало
>     
>      def get_age(self):
>          now = datetime.datetime.now()
>          return now.year-self.yob 
## Ошибка в методе <i>set_name</i>

>   ## В этом методе не переопределялось имя
>   ### Было
>     
>      def set_name(self, name):
>          self.name = self.name
>   ### Стало
>     
>      def set_name(self, name):
>          self.name = name
## Ошибка в методе <i>set_address</i>

>   ## В этом методе не переопределялося адрес
>   ### Было
>     
>      def set_address(self, address):
>          self.address == address
>   ### Стало
>     
>      def set_address(self, address):
>          self.address = address
## Ошибка в методе <i>is_homeless</i>

>   ## В этом методе программа не могла опредилить перемнную adress
>   ### Было
>     
>      def is_homeless(self):
>           return address is None
>   ### Стало
>     
>      def is_homeless(self):
>           return self.address is None