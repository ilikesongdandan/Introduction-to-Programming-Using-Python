import tensorflow as tf

__author__ = 'wangj'
__date__ = '2018/05/02 19:55'


def main():
    pass


class Network(object):
    def __init__(self, learning_rate=0.001, ):
        # 记录训练次数
        self.global_step = tf.Variable(0, trainable=False, name='global_step')
        # 学习速率
        self.learning_rate = learning_rate
        # 输入张量 28 * 28 = 784个像素的图片一维向量
        self.x = tf.placeholder(tf.float32, [None, 784], name='x')
        # 标签值，即图像对应的结果，如果对应数字是8，则对应label是 [0,0,0,0,0,0,0,0,1,0]
        # 这种方式称为 one-hot编码
        # 标签是一个长度为10的一维向量，值最大的下标即图片上写的数字
        self.label = tf.placeholder(tf.float32, [None, 10], name='label')

        # 权重，初始化 正态分布
        self.w = tf.Variable(tf.random_normal([784, 10]), name='fc/weight')
        # 偏置 bias， 初始化 正态分布
        self.b = tf.Variable(tf.random_normal([10]), name='fc/bias')
        # 输出 y = softmax(X * w + b)
        self.y = tf.nn.softmax(tf.matmul(self.x, self.w) + self.b, name='y')
        # 损失，即交叉熵，最常用的计算标签(label)与输出(y)之间差别的方法
        self.loss = - tf.reduce_sum(self.label * tf.log(self.y + 1e-10))
        # 反向传播，采用梯度下降的方法。调整w与b，使得损失(loss)最小
        # loss越小，那么计算出来的y值与 标签(label)值越接近，准确率越高
        # minimize 可传入参数 global_step， 每次训练 global_step的值会增加1
        # 因此，可以通过计算self.global_step这个张量的值，知道当前训练了多少步
        self.train = tf.train.GradientDescentOptimizer(self.learning_rate).minimize(self.loss, global_step=self.global_step)

        # 以下代码验证正确率时使用
        # argmax 返回最大值的下标，最大值的下标即答案
        # 例如 [0,0,0,0.9,0,0.1,0,0,0,0] 代表数字3
        predict = tf.equal(tf.argmax(self.label, 1), tf.argmax(self.y, 1))

        # predict -> [true, true, true, false, false, true]
        # reduce_mean即求predict的平均数 即 正确个数 / 总数，即正确率
        self.accuracy = tf.reduce_mean(tf.cast(predict, dtype=tf.float32))

        # 创建loss的summary node，scalar表示最后的数据会展示为标量曲线。
        # w, b 画直方图
        # loss, accuracy画标量图
        tf.summary.histogram('weight', self.w)
        tf.summary.histogram('bias', self.b)
        tf.summary.scalar('loss', self.loss)
        tf.summary.scalar('accuracy', self.accuracy)

if __name__ == '__main__':
    pass
