#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->radioButton_1_Sl->click();//убираем клик на радиокномке
    ui->label_error->setVisible(false);//убираем сообщение об ошибке
    ui->label_res->setVisible(false);
}

MainWindow::~MainWindow()
{
    delete ui;

}

void MainWindow::on_pushButton_result_clicked()//кнопка результата
{
    int op_1, op_2, res; // операнты и результат
    QString str; // строка для конвертации
    bool fli; //флаг успешности преобразования

    if(ui->radioButton_1_Sl->isChecked())//выбор сложения
    {
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toInt(&fli);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fli) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();//копируем в строку текст из поля 2
            op_2=str.toInt(&fli);//пытаемся преобразовать 2 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
            if(fli)
            {
                res=op_1+op_2;
                ui->label_error->setVisible(false);//скрываем сообщение об ошибке
                ui->label_res->setNum(res); //вывод результата
                ui->label_res->setVisible(true);//показываем результат
            }
            else
            {
                ui->label_res->setVisible(false);//скрываем результат
                ui->label_error->setText("Ошибка в Cлагаемом 2");
                ui->label_error->setVisible(true);//показываем ошибку
            }
        }
        else
        {
            ui->label_res->setVisible(false);//скрываем результат
            ui->label_error->setText("Ошибка в Cлагаемом 1");
            ui->label_error->setVisible(true);//показываем ошибку
        }
    }

    if(ui->radioButton_2_Bh->isChecked())//выбор вычитание
    {
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toInt(&fli);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fli) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();//копируем в строку текст из поля 2
            op_2=str.toInt(&fli);//пытаемся преобразовать 2 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
            if(fli)
            {
                res=op_1-op_2;
                ui->label_error->setVisible(false);//скрываем сообщение об ошибке
                ui->label_res->setNum(res); //вывод результата
                ui->label_res->setVisible(true);//показываем результат
            }
            else
            {
                ui->label_res->setVisible(false);//скрываем результат
                ui->label_error->setText("Ошибка в Вычитаемом");
                ui->label_error->setVisible(true);//показываем ошибку
            }
        }
        else
        {
            ui->label_res->setVisible(false);//скрываем результат
            ui->label_error->setText("Ошибка в Уменьшаемом");
            ui->label_error->setVisible(true);//показываем ошибку
        }
    }

    if(ui->radioButton_3_Dl->isChecked())//выбор деление
    {
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toInt(&fli);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fli) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();//копируем в строку текст из поля 2
            op_2=str.toInt(&fli);//пытаемся преобразовать 2 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
            if(fli)
            {

            if(op_2==0)
                {
                    ui->label_res->setVisible(false);//скрываем результат
                    ui->label_error->setText("На ноль делить нельзя!!!");
                    ui->label_error->setVisible(true);//показываем ошибку
                }
                else
                {
                    res=op_1/op_2;
                    ui->label_error->setVisible(false);//скрываем сообщение об ошибке
                    ui->label_res->setNum(res); //вывод результата
                    ui->label_res->setVisible(true);//показываем результат
                }

            }
            else
            {
                ui->label_res->setVisible(false);//скрываем результат
                ui->label_error->setText("Ошибка в Делителе");
                ui->label_error->setVisible(true);//показываем ошибку
            }
        }
        else
        {
            ui->label_res->setVisible(false);//скрываем результат
            ui->label_error->setText("Ошибка в Делимом");
            ui->label_error->setVisible(true);//показываем ошибку
        }

    }

    if(ui->radioButton_4_Ym->isChecked())//выбор умножение
    {
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toInt(&fli);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fli) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();//копируем в строку текст из поля 2
            op_2=str.toInt(&fli);//пытаемся преобразовать 2 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
            if(fli)
            {
                res=op_1*op_2;
                ui->label_error->setVisible(false);//скрываем сообщение об ошибке
                ui->label_res->setNum(res); //вывод результата
                ui->label_res->setVisible(true);//показываем результат
            }

            else
            {
                ui->label_res->setVisible(false);//скрываем результат
                ui->label_error->setText("Ошибка в множителе 2");
                ui->label_error->setVisible(true);//показываем ошибку
            }
        }
        else
        {
            ui->label_res->setVisible(false);//скрываем результат
            ui->label_error->setText("Ошибка в множителе 1");
            ui->label_error->setVisible(true);//показываем ошибку
        }
    }
}

void MainWindow::on_radioButton_1_Sl_clicked()//Замена названия кнопки, замена op 1 и 2(сложение)
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("Слагаемое 1");
    ui->label_op_2->setText("Слагаемое 2");
    ui->pushButton_result->setText("Сумма");

}

void MainWindow::on_radioButton_2_Bh_clicked()//Замена названия кнопки, замена op 1 и 2(вычитание)
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("Уменьшаемое");
    ui->label_op_2->setText("Вычитаемое");
    ui->pushButton_result->setText("Вычитание");
}


void MainWindow::on_radioButton_3_Dl_clicked()//Замена названия кнопки, замена op 1 и 2(деление)
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("Делимое");
    ui->label_op_2->setText("Делитель");
    ui->pushButton_result->setText("Деление");
}


void MainWindow::on_radioButton_4_Ym_clicked()//Замена названия кнопки, замена op 1 и 2(умножение)
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("1-ый множитель");
    ui->label_op_2->setText("2-ой множитель");
    ui->pushButton_result->setText("Умножение");
}

void MainWindow::on_pushButton_ohistka_clicked()//очистка
{
    ui->lineEdit_op_1->clear();//очистка op 1
    ui->lineEdit_op_2->clear();//очистка op 2
    ui->label_res->clear();//очистка результата
    ui->label_error->clear();//очистка ошибки
}

