
from amis.AmisComponent import AmisComponent

class Video(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "video")
        
    
    def className(self, className):
        # 容器 css 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("className", className)

        
    def disabled(self, disabled):
        # 是否禁用
        
        return self.set("disabled", disabled)

        
    def disabledOn(self, disabledOn):
        # 是否禁用表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("disabledOn", disabledOn)

        
    def hidden(self, hidden):
        # 是否隐藏
        
        return self.set("hidden", hidden)

        
    def hiddenOn(self, hiddenOn):
        # 是否隐藏表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("hiddenOn", hiddenOn)

        
    def visible(self, visible):
        # 是否显示
        
        return self.set("visible", visible)

        
    def visibleOn(self, visibleOn):
        # 是否显示表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("visibleOn", visibleOn)

        
    def id(self, id):
        # 组件唯一 id，主要用于日志采集
        
        return self.set("id", id)

        
    def onEvent(self, onEvent):
        # 事件动作配置
        
        return self.set("onEvent", onEvent)

        
    def static(self, static):
        # 是否静态展示
        
        return self.set("static", static)

        
    def staticOn(self, staticOn):
        # 是否静态展示表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("staticOn", staticOn)

        
    def staticPlaceholder(self, staticPlaceholder):
        # 静态展示空值占位
        
        return self.set("staticPlaceholder", staticPlaceholder)

        
    def staticClassName(self, staticClassName):
        # 静态展示表单项类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("staticClassName", staticClassName)

        
    def staticLabelClassName(self, staticLabelClassName):
        # 静态展示表单项Label类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("staticLabelClassName", staticLabelClassName)

        
    def staticInputClassName(self, staticInputClassName):
        # 静态展示表单项Value类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("staticInputClassName", staticInputClassName)

        
    def staticSchema(self, staticSchema):
        
        
        return self.set("staticSchema", staticSchema)

        
    def style(self, style):
        # 组件样式
        
        return self.set("style", style)

        
    def editorSetting(self, editorSetting):
        # 编辑器配置，运行时可以忽略
        
        return self.set("editorSetting", editorSetting)

        
    def useMobileUI(self, useMobileUI):
        # 可以组件级别用来关闭移动端样式
        
        return self.set("useMobileUI", useMobileUI)

        
    def testIdBuilder(self, testIdBuilder):
        
        
        return self.set("testIdBuilder", testIdBuilder)

        
    def type(self, type):
        # 指定为视频类型
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def autoPlay(self, autoPlay):
        # 是否自动播放
        
        return self.set("autoPlay", autoPlay)

        
    def columnsCount(self, columnsCount):
        # 如果显示切帧，通过此配置项可以控制每行显示多少帧
        
        return self.set("columnsCount", columnsCount)

        
    def frames(self, frames):
        # 设置后，可以显示切帧.点击帧的时候会将视频跳到对应时间。  frames: {  '01:22': 'http://domain/xxx.jpg' }
        
        return self.set("frames", frames)

        
    def framesClassName(self, framesClassName):
        # 配置帧列表容器className
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("framesClassName", framesClassName)

        
    def isLive(self, isLive):
        # 如果是实时的，请标记一下
        
        return self.set("isLive", isLive)

        
    def jumpFrame(self, jumpFrame):
        # 点击帧画面时是否跳转视频对应的点
        
        return self.set("jumpFrame", jumpFrame)

        
    def muted(self, muted):
        # 是否初始静音
        
        return self.set("muted", muted)

        
    def loop(self, loop):
        # 是否循环播放
        
        return self.set("loop", loop)

        
    def playerClassName(self, playerClassName):
        # 配置播放器 className
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("playerClassName", playerClassName)

        
    def poster(self, poster):
        # 视频封面地址
        
        return self.set("poster", poster)

        
    def splitPoster(self, splitPoster):
        # 是否将视频和封面分开显示
        
        return self.set("splitPoster", splitPoster)

        
    def src(self, src):
        # 视频播放地址
        
        return self.set("src", src)

        
    def videoType(self, videoType):
        # 视频类型如： video/x-flv
        
        return self.set("videoType", videoType)

        
    def aspectRatio(self, aspectRatio):
        # 视频比率# 可选项: ['auto', '4:3', '16:9']
        
        return self.set("aspectRatio", aspectRatio)

        
    def rates(self, rates):
        # 视频速率
        
        return self.set("rates", rates)

        
    def jumpBufferDuration(self, jumpBufferDuration):
        # 跳转到帧时，往前多少秒。
        
        return self.set("jumpBufferDuration", jumpBufferDuration)

        
    def stopOnNextFrame(self, stopOnNextFrame):
        # 默认播放的时候到了下一帧会继续播放，同时高亮下一帧。 如果配置这个则会停止播放，等待用户选择新的区间再播放。
        
        return self.set("stopOnNextFrame", stopOnNextFrame)

        