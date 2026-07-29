Windows PowerShell
Copyright (C) Microsoft Corporation. Todos os direitos reservados.


PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"1984","autor":"George Orwell","ano":1949}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-29 09:31:33.343607
id           : 17
titulo       : 1984



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"O Senhor dos Anéis","autor":"J.R.R. Tolkien","ano":1954}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1954
autor        : J.R.R. Tolkien
data_criacao : 2026-07-29 09:31:57.821579
id           : 18
titulo       : O Senhor dos Anéis



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"Dom Casmurro","autor":"Machado de Assis","ano":1899}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-29 09:32:05.720974
id           : 19
titulo       : Dom Casmurro



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"O Pequeno Príncipe","autor":"Antoine de Saint-Exupéry","ano":1943}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1943
autor        : Antoine de Saint-Exupéry
data_criacao : 2026-07-29 09:32:12.891756
id           : 20
titulo       : O Pequeno Príncipe



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"Moby Dick","autor":"Herman Melville","ano":1851}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1851
autor        : Herman Melville
data_criacao : 2026-07-29 09:32:20.822956
id           : 21
titulo       : Moby Dick



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"O Cortiço","autor":"Aluísio Azevedo","ano":1890}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-29 09:32:27.519227
id           : 22
titulo       : O Cortiço



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"A Metamorfose","autor":"Franz Kafka","ano":1915}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1915
autor        : Franz Kafka
data_criacao : 2026-07-29 09:32:34.302382
id           : 23
titulo       : A Metamorfose



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"Grande Sertão: Veredas","autor":"Guimarães Rosa","ano":1956}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1956
autor        : Guimarães Rosa
data_criacao : 2026-07-29 09:32:42.734930
id           : 24
titulo       : Grande Sertão: Veredas



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"Vidas Secas","autor":"Graciliano Ramos","ano":1938}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1938
autor        : Graciliano Ramos
data_criacao : 2026-07-29 09:32:50.374113
id           : 25
titulo       : Vidas Secas



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"Capitães da Areia","autor":"Jorge Amado","ano":1937}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json; charset=utf-8" -Body $body


ano          : 1937
autor        : Jorge Amado
data_criacao : 2026-07-29 09:32:56.371253
id           : 26
titulo       : Capitães da Areia



PS H:\Python\Etapa2\Aula15-API> $body = [System.Text.Encoding]::UTF8.GetBytes('{"titulo":"Cotemig","autor":"3A1","ano":2026}')
>> Invoke-RestMethod http://127.0.0.1:5000/api/livros/1 -Method PUT -ContentType "application/json; charset=utf-8" -Body $body
>>


ano          : 2026
autor        : 3A1
data_criacao : 2026-07-29 09:12:57.281237
id           : 1
titulo       : Cotemig



PS H:\Python\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros
>>


ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-29 09:12:57.281237
id           : 3
titulo       : 1984

ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-29 09:19:34.032525
id           : 5
titulo       : 1984

ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-29 09:20:23.757260
id           : 10
titulo       : 1984

ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-29 09:21:48.062610
id           : 15
titulo       : 1984

ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-29 09:26:21.629823
id           : 16
titulo       : 1984

ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-29 09:31:33.343607
id           : 17
titulo       : 1984

ano          : 1915
autor        : Franz Kafka
data_criacao : 2026-07-29 09:19:34.118576
id           : 8
titulo       : A Metamorfose

ano          : 1915
autor        : Franz Kafka
data_criacao : 2026-07-29 09:20:23.835572
id           : 13
titulo       : A Metamorfose

ano          : 1915
autor        : Franz Kafka
data_criacao : 2026-07-29 09:32:34.302382
id           : 23
titulo       : A Metamorfose

ano          : 1937
autor        : Jorge Amado
data_criacao : 2026-07-29 09:32:56.371253
id           : 26
titulo       : Capitães da Areia

ano          : 2026
autor        : 3A1
data_criacao : 2026-07-29 09:12:57.281237
id           : 1
titulo       : Cotemig

ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-29 09:19:34.048866
id           : 6
titulo       : Dom Casmurro

ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-29 09:20:23.785894
id           : 11
titulo       : Dom Casmurro

ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-29 09:32:05.720974
id           : 19
titulo       : Dom Casmurro

ano          : 1956
autor        : Guimarães Rosa
data_criacao : 2026-07-29 09:32:42.734930
id           : 24
titulo       : Grande Sertão: Veredas

ano          : 1851
autor        : Herman Melville
data_criacao : 2026-07-29 09:19:34.087099
id           : 7
titulo       : Moby Dick

ano          : 1851
autor        : Herman Melville
data_criacao : 2026-07-29 09:20:23.814802
id           : 12
titulo       : Moby Dick

ano          : 1851
autor        : Herman Melville
data_criacao : 2026-07-29 09:32:20.822956
id           : 21
titulo       : Moby Dick

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-29 09:12:57.281237
id           : 2
titulo       : O Cortiço

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-29 09:32:27.519227
id           : 22
titulo       : O Cortiço

ano          : 1943
autor        : Antoine de Saint-Exupéry
data_criacao : 2026-07-29 09:32:12.891756
id           : 20
titulo       : O Pequeno Príncipe

ano          : 1954
autor        : J.R.R. Tolkien
data_criacao : 2026-07-29 09:31:57.821579
id           : 18
titulo       : O Senhor dos Anéis

ano          : 1938
autor        : Graciliano Ramos
data_criacao : 2026-07-29 09:19:34.151750
id           : 9
titulo       : Vidas Secas

ano          : 1938
autor        : Graciliano Ramos
data_criacao : 2026-07-29 09:20:23.867856
id           : 14
titulo       : Vidas Secas

ano          : 1938
autor        : Graciliano Ramos
data_criacao : 2026-07-29 09:32:50.374113
id           : 25
titulo       : Vidas Secas

ano          : 1300
autor        : ru
data_criacao : 2026-07-29 09:17:36.166119
id           : 4
titulo       : mare



PS H:\Python\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0 -Method DELETE
>> Invoke-RestMethod http://127.0.0 -Method DELETE
>> Invoke-RestMethod http://127.0.0 -Method DELETE
>>
Invoke-RestMethod : Impossível conectar-se ao servidor remoto
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0 -Method DELETE
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
 
Invoke-RestMethod : Impossível conectar-se ao servidor remoto
No linha:2 caractere:1
+ Invoke-RestMethod http://127.0.0 -Method DELETE
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
 
Invoke-RestMethod : Impossível conectar-se ao servidor remoto
No linha:3 caractere:1
+ Invoke-RestMethod http://127.0.0 -Method DELETE
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
 
PS H:\Python\Etapa2\Aula15-API>
PS H:\Python\Etapa2\Aula15-API> Invoke-RestMethod http://127.0.0:5000 -Method DELETE
>> Invoke-RestMethod http://127.0.0:5000 -Method DELETE
>> Invoke-RestMethod http://127.0.0:5000 -Method DELETE
>>
Invoke-RestMe