#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
using namespace std;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui -> comboBox_oper -> setCurrentIndex(1);
}

MainWindow::~MainWindow()
{
    delete ui;
}
void MainWindow::my_func()//тело функции
{
    bool op1, op2;//операнды
    int index;
    int res; //результат
    /*false - red, true - green
    if(ui -> comboBox_op1 -> currentIndex() == 0)
        op1 = false;
    else
        op1 = true;
    так делать не надо*/
    op1 = ui -> comboBox_op1 -> currentIndex() == 1;
    op2 = ui -> comboBox_op2 -> currentIndex() == 1;
    index = ui-> comboBox_oper -> currentIndex();

    QPalette pal; //палитра
    pal = ui -> centralwidget -> palette();// текущая палитра
    ui -> comboBox_op2 -> setVisible(true);

    switch (index) //обрабатываем тип логической операции
    {
    case 0: //дизъюнкция
    {
        if(op1 || op2)
            res = true;
        else
            res = false;
        break;
    }
    case 1: //конъюкция
    {
        if(op1 && op2)
            res = true;
        else
            res = false;
        break;
    }
    case 2://инверсия
    {
        ui-> comboBox_op2 -> setVisible(false);
        if(op1)
            res = false;
        else
            res = true;
        break;
    }
    case 3://импликация
    {
        if ((op1 == true) && (op2 == false))
            res = false;
        else
            res = true;
        break;
    }
    case 4: //эквивалентность
    {
        if(op1 == op2)
            res = true;
        else
            res = false;
        break;
    }
    case 5://Строгая дизъюнкция(XOR)
    {
        if(((op1 == true) && (op2 == false)) || ((op1 == false) && (op2 == true)))
            res = true;
        else
            res = false;
        break;
    }
    }

    if(res == true)//окрашиваем фон в зависимости от результата
        pal.setColor(QPalette::Window, Qt::green);
    else
        pal.setColor(QPalette::Window, Qt::red);


ui -> centralwidget -> setAutoFillBackground(true);
ui -> centralwidget ->setPalette(pal);
}

void MainWindow::on_comboBox_oper_currentIndexChanged(int index)
{
    my_func();
}

void MainWindow::on_comboBox_op1_currentIndexChanged(int index)
{
    my_func();
}


void MainWindow::on_comboBox_op2_currentIndexChanged(int index)
{
    my_func();
}

