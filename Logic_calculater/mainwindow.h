#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_comboBox_oper_currentIndexChanged(int index);

    void on_comboBox_op1_currentIndexChanged(int index);

    void on_comboBox_op2_currentIndexChanged(int index);

private:
    Ui::MainWindow *ui;
    void my_func(void);//объявление нашей функции
};

#endif // MAINWINDOW_H
