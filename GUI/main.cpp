#include <QApplication>
#include <QLabel>
#include <form.h>
int main(int argc, char* argv[])
{
    QApplication app(argc, argv);
    QLabel *label = new QLabel("Hello World");
    label->setWindowTitle("MY App");
    label->resize(400, 400);
    label->show();

    Form F;
    F.show();
    return app.exec();
}
