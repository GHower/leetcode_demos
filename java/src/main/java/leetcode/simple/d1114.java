package leetcode.simple;

import java.util.concurrent.atomic.AtomicInteger;

public class d1114 {
    public d1114() {

    }
    volatile AtomicInteger n = new AtomicInteger(1);
    public void first(Runnable printFirst) throws InterruptedException {

        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        n.addAndGet(1);
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while (n.get()!=2);
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        n.addAndGet(1);
    }

    public void third(Runnable printThird) throws InterruptedException {
        while (n.get()!=3);
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
