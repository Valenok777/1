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
    void on_pushButton_result_clicked();

    void on_radioButton_1_Sl_clicked();

    void on_radioButton_2_Bh_clicked();

    void on_radioButton_3_Dl_clicked();

    void on_radioButton_4_Ym_clicked();

    void on_pushButton_ohistka_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
