#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->radioButton_1_Sl->click();
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
}

MainWindow::~MainWindow()
{
    delete ui;

}

void MainWindow::on_pushButton_result_clicked()
{
    int op_1, op_2, res; // операнты и результат
    QString str; // строка для конвертации
    bool fli; //флаг успешности преобразования
    if(ui->radioButton_1_Sl->isChecked())
    {
        str=ui->lineEdit_op_1->text();
        op_1=str.toInt(&fli);

        if(fli) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();
            op_2=str.toInt(&fli);


            if(fli)
            {
            res=op_1+op_2;
            ui->label_error->setVisible(false);
            ui->label_res->setNum(res); //вывод результата
            ui->label_res->setVisible(true);

            }

            else
            {
                ui->label_res->setVisible(false);
                ui->label_error->setText("Ошибка в слогаемом 2");
                ui->label_error->setVisible(true);
            }

        }
        else
        {
            ui->label_res->setVisible(false);
            ui->label_error->setText("Ошибка в слогаемом 1");
            ui->label_error->setVisible(true);
        }

    }

    if(ui->radioButton_2_Bh->isChecked())
    {
        str=ui->lineEdit_op_1->text();
        op_1=str.toInt(&fli);

        if(fli) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();
            op_2=str.toInt(&fli);


            if(fli)
            {
            res=op_1-op_2;
            ui->label_error->setVisible(false);
            ui->label_res->setNum(res); //вывод результата
            ui->label_res->setVisible(true);

            }

            else
            {
                ui->label_res->setVisible(false);
                ui->label_error->setText("Ошибка в слогаемом 2");
                ui->label_error->setVisible(true);
            }

        }
        else
        {
            ui->label_res->setVisible(false);
            ui->label_error->setText("Ошибка в слогаемом 1");
            ui->label_error->setVisible(true);
        }

    }

    if(ui->radioButton_3_Dl->isChecked())
    {
        str=ui->lineEdit_op_1->text();
        op_1=str.toInt(&fli);

        if(fli) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();
            op_2=str.toInt(&fli);


            if(fli)
            {
            res=op_1/op_2;
            ui->label_error->setVisible(false);
            ui->label_res->setNum(res); //вывод результата
            ui->label_res->setVisible(true);

            }

            else
            {
                ui->label_res->setVisible(false);
                ui->label_error->setText("Ошибка в слогаемом 2");
                ui->label_error->setVisible(true);
            }

        }
        else
        {
            ui->label_res->setVisible(false);
            ui->label_error->setText("Ошибка в слогаемом 1");
            ui->label_error->setVisible(true);
        }

    }
    if(ui->radioButton_4_Ym->isChecked())
    {
        str=ui->lineEdit_op_1->text();
        op_1=str.toInt(&fli);

        if(fli) //проверка успешности преобразования
        {
            str=ui->lineEdit_op_2->text();
            op_2=str.toInt(&fli);


            if(fli)
            {
            res=op_1*op_2;
            ui->label_error->setVisible(false);
            ui->label_res->setNum(res); //вывод результата
            ui->label_res->setVisible(true);

            }

            else
            {
                ui->label_res->setVisible(false);
                ui->label_error->setText("Ошибка в слогаемом 2");
                ui->label_error->setVisible(true);
            }

        }
        else
        {
            ui->label_res->setVisible(false);
            ui->label_error->setText("Ошибка в слогаемом 1");
            ui->label_error->setVisible(true);
        }

    }
}

void MainWindow::on_radioButton_1_Sl_clicked()
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("Слагаеиое 1");
    ui->label_op_2->setText("Слагаемое 2");
    ui->pushButton_result->setText("Сумма");

}

void MainWindow::on_radioButton_2_Bh_clicked()
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("Слагаеиое 1");
    ui->label_op_2->setText("Слагаемое 2");
    ui->pushButton_result->setText("Вычитание");
}


void MainWindow::on_radioButton_3_Dl_clicked()
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("Слагаеиое 1");
    ui->label_op_2->setText("Слагаемое 2");
    ui->pushButton_result->setText("Деление");
}


void MainWindow::on_radioButton_4_Ym_clicked()
{
    ui->label_error->setVisible(false);
    ui->label_res->setVisible(false);
    ui->label_op_1->setText("Слагаеиое 1");
    ui->label_op_2->setText("Слагаемое 2");
    ui->pushButton_result->setText("Умножение");
}

void MainWindow::on_pushButton_ohistka_clicked()
{
    ui->lineEdit_op_1->clear();
    ui->lineEdit_op_2->clear();
    ui->label_res->clear();
}
