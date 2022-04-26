#!/bin/bash

converte_imagem(){
cd ~/Downloads/imagens-livros
if [ ! -d png ];then
	mkdir png
fi

for imagem in *.jpeg;do
	imagem_sem_extensao=$(ls "$imagem" | awk -F. '{ print $1 }')
	convert "$imagem_sem_extensao".jpeg png/"$imagem_sem_extensao".png
done
}

converte_imagem 
if [ "$?" -eq 0 ];then
	echo 'Conversao realizada com sucesso'
else
	echo 'Houve uma falha no processo e o codigo de erro foi: '"$?"
fi
