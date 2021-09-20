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
    double op_1 , op_2;
    double res;
    QString str;// строка для конвертации
    bool fl1;//флаг успешности преобразования
    bool fl2;//флаг успешности преобразования

    if(ui->radioButton_1_Sl->isChecked())//выбор сложения
    {
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toDouble(&fl1);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fl1) //проверка успешности преобразования
        {
            ui->lineEdit_op_2->setVisible(true);
            ui->label_op_2->setVisible(true);
            str=ui->lineEdit_op_2->text();//копируем в строку текст из поля 2
            op_2=str.toDouble(&fl2);//пытаемся преобразовать 2 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
            if(fl2)
            {
                res=op_1+op_2;
                ui->label_error->setVisible(false);//скрываем сообщение об ошибке
                ui->label_res->setNum(res); //вывод результата
                ui->label_res->setText(QString::number(res));
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
        ui->lineEdit_op_2->setVisible(true);
        ui->label_op_2->setVisible(true);
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toDouble(&fl1);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fl1) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();//копируем в строку текст из поля 2
            op_2=str.toDouble(&fl2);//пытаемся преобразовать 2 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
            if(fl2)
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
        ui->lineEdit_op_2->setVisible(true);
        ui->label_op_2->setVisible(true);
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toDouble(&fl1);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fl1) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();//копируем в строку текст из поля 2
            op_2=str.toDouble(&fl2);//пытаемся преобразовать 2 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
            if(fl2)
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
        ui->lineEdit_op_2->setVisible(true);
        ui->label_op_2->setVisible(true);
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toDouble(&fl1);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fl1) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();//копируем в строку текст из поля 2
            op_2=str.toDouble(&fl2);//пытаемся преобразовать 2 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
            if(fl2)
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
    if(ui->radioButton_5_sqrt->isChecked())//корень
    {
        ui->lineEdit_op_2->setVisible(false);
        ui->label_op_2->setVisible(false);
        double res1 = 0;
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toDouble(&fl1);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fl1)
        {
            res1=sqrt(op_1);
            ui->label_error->setVisible(false);//скрываем сообщение об ошибке
            ui->label_res->setNum(res1); //вывод результата
            ui->label_res->setVisible(true);//показываем результат
        }

        else
        {
            ui->label_res->setVisible(false);//скрываем результат
            ui->label_error->setText("Ошибка в подкоренном числе");
            ui->label_error->setVisible(true);//показываем ошибку
        }

    }
    if(ui->radioButton_6_sin->isChecked())//sin
    {
        ui->lineEdit_op_2->setVisible(false);
        ui->label_op_2->setVisible(false);
        double res1 = 0;
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toDouble(&fl1);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fl1)
        {
            res1=sin(op_1);
            ui->label_error->setVisible(false);//скрываем сообщение об ошибке
            ui->label_res->setNum(res1); //вывод результата
            ui->label_res->setVisible(true);//показываем результат
        }

        else
        {
            ui->label_res->setVisible(false);//скрываем результат
            ui->label_error->setText("Ошибка в аргументе");
            ui->label_error->setVisible(true);//показываем ошибку
        }

    }
    if(ui->radioButton_7_cos->isChecked())//cos
    {
        ui->lineEdit_op_2->setVisible(false);
        ui->label_op_2->setVisible(false);
        double res1 = 0;
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toDouble(&fl1);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fl1)
        {
            res1=cos(op_1);
            ui->label_error->setVisible(false);//скрываем сообщение об ошибке
            ui->label_res->setNum(res1); //вывод результата
            ui->label_res->setVisible(true);//показываем результат
        }

        else
        {
            ui->label_res->setVisible(false);//скрываем результат
            ui->label_error->setText("Ошибка в аргументе");
            ui->label_error->setVisible(true);//показываем ошибку
        }

    }
    if(ui->radioButton_8_arsin->isChecked())//arsin
    {
        ui->lineEdit_op_2->setVisible(false);
        ui->label_op_2->setVisible(false);
        double res1 = 0;
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toDouble(&fl1);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fl1)
        {
            res1=asin(op_1);
            ui->label_error->setVisible(false);//скрываем сообщение об ошибке
            ui->label_res->setNum(res1); //вывод результата
            ui->label_res->setVisible(true);//показываем результат
        }

        else
        {
            ui->label_res->setVisible(false);//скрываем результат
            ui->label_error->setText("Ошибка в аргументе");
            ui->label_error->setVisible(true);//показываем ошибку
        }

    }
    if(ui->radioButton_9_arcos->isChecked())//arcos
    {
        ui->lineEdit_op_2->setVisible(false);
        ui->label_op_2->setVisible(false);
        double res1 = 0;
        str=ui->lineEdit_op_1->text();//копируем в строку текст из поля 1
        op_1=str.toDouble(&fl1);//пытаемся преобразовать 1 операнд в целостной тип данных и присваиваем число к соответствуещей переменной
        if(fl1)
        {
            res1=acos(op_1);
            ui->label_error->setVisible(false);//скрываем сообщение об ошибке
            ui->label_res->setNum(res1); //вывод результата
            ui->label_res->setVisible(true);//показываем результат
        }

        else
        {
            ui->label_res->setVisible(false);//скрываем результат
            ui->label_error->setText("Ошибка в аргументе");
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
    ui->lineEdit_op_2->setVisible(true);
    ui->label_op_2->setVisible(true);
    ui->pushButton_result->setText("Узнать результат");

}

void MainWindow::on_radioButton_2_Bh_clicked()//Замена названия кнопки, замена op 1 и 2(вычитание)
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("Уменьшаемое");
    ui->label_op_2->setText("Вычитаемое");
    ui->lineEdit_op_2->setVisible(true);
    ui->label_op_2->setVisible(true);
    ui->pushButton_result->setText("Узнать результат");
}


void MainWindow::on_radioButton_3_Dl_clicked()//Замена названия кнопки, замена op 1 и 2(деление)
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("Делимое");
    ui->label_op_2->setText("Делитель");
    ui->lineEdit_op_2->setVisible(true);
    ui->label_op_2->setVisible(true);
    ui->pushButton_result->setText("Узнать результат");
}


void MainWindow::on_radioButton_4_Ym_clicked()//Замена названия кнопки, замена op 1 и 2(умножение)
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("1-ый множитель");
    ui->label_op_2->setText("2-ой множитель");
    ui->lineEdit_op_2->setVisible(true);
    ui->label_op_2->setVisible(true);
    ui->pushButton_result->setText("Узнать результат");
}

void MainWindow::on_pushButton_ohistka_clicked()//очистка
{
    if(ui->radioButton_5_sqrt->isChecked() or ui->radioButton_6_sin->isChecked() or ui->radioButton_7_cos->isChecked() or ui->radioButton_8_arsin->isChecked() or ui->radioButton_9_arcos->isChecked())
    {
        ui->lineEdit_op_2->setVisible(false);
        ui->label_op_2->setVisible(false);
        ui->lineEdit_op_1->clear();//очистка op 1
        ui->label_res->clear();//очистка результата
        ui->label_error->clear();//очистка ошибки

     }
    else
    {
        ui->lineEdit_op_1->clear();//очистка op 1
        ui->lineEdit_op_2->clear();//очистка op 2
        ui->label_res->clear();//очистка результата
        ui->label_error->clear();//очистка ошибки
        ui->lineEdit_op_2->setVisible(true);
        ui->label_op_2->setVisible(true);
    }
}


void MainWindow::on_radioButton_5_sqrt_clicked()
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->lineEdit_op_2->setVisible(false);
    ui->label_op_2->setVisible(false);
    ui->label_op_1->setText("аргумент");
    ui->pushButton_result->setText("Узнать результат");
}

void MainWindow::on_radioButton_6_sin_clicked()
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->lineEdit_op_2->setVisible(false);
    ui->label_op_2->setVisible(false);
    ui->label_op_1->setText("аргумент");
    ui->pushButton_result->setText("Узнать результат");
}

void MainWindow::on_radioButton_7_cos_clicked()
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->lineEdit_op_2->setVisible(false);
    ui->label_op_2->setVisible(false);
    ui->label_op_1->setText("аргумент");
    ui->pushButton_result->setText("Узнать результат");
}

void MainWindow::on_radioButton_8_arsin_clicked()
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->lineEdit_op_2->setVisible(false);
    ui->label_op_2->setVisible(false);
    ui->label_op_1->setText("аргумент");
    ui->pushButton_result->setText("Узнать результат");
}

void MainWindow::on_radioButton_9_arcos_clicked()
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->lineEdit_op_2->setVisible(false);
    ui->label_op_2->setVisible(false);
    ui->label_op_1->setText("аргумент");
    ui->pushButton_result->setText("Узнать результат");
}

