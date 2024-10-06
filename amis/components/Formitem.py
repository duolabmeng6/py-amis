
from amis.AmisComponent import AmisComponent

class Formitem(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "formitem")
    
    def type(self, type):
        # 指定表单项类型 可选项: string
        return self.set("type", type)

        
    def className(self, className):
        # 表单最外层类名 可选项: string
        return self.set("className", className)

        
    def inputClassName(self, inputClassName):
        # 表单控制器类名 可选项: string
        return self.set("inputClassName", inputClassName)

        
    def labelClassName(self, labelClassName):
        # label 的类名 可选项: string
        return self.set("labelClassName", labelClassName)

        
    def name(self, name):
        # 字段名，指定该表单项提交时的 key 可选项: string
        return self.set("name", name)

        
    def value(self, value):
        # 表单默认值 可选项: string
        return self.set("value", value)

        
    def label(self, label):
        # 表单项标签 可选项: [模板](../../../docs/concepts/template)或false
        return self.set("label", label)

        
    def labelAlign(self, labelAlign):
        # 表单项标签对齐方式，默认右对齐，仅在 `mode`为`horizontal` 时生效 可选项: "right","left"
        return self.set("labelAlign", labelAlign)

        
    def labelRemark(self, labelRemark):
        # 表单项标签描述 可选项: [Remark](../remark)
        return self.set("labelRemark", labelRemark)

        
    def description(self, description):
        # 表单项描述 可选项: [模板](../../../docs/concepts/template)
        return self.set("description", description)

        
    def placeholder(self, placeholder):
        # 表单项描述 可选项: string
        return self.set("placeholder", placeholder)

        
    def inline(self, inline):
        # 是否为 内联 模式 可选项: boolean
        return self.set("inline", inline)

        
    def strictMode(self, strictMode):
        # 通过配置 false 可以及时获取所有表单里面的数据，否则可能会有不同步 可选项: boolean
        return self.set("strictMode", strictMode)

        
    def submitOnChange(self, submitOnChange):
        # 是否该表单项值发生变化时就提交当前表单。 可选项: boolean
        return self.set("submitOnChange", submitOnChange)

        
    def disabled(self, disabled):
        # 当前表单项是否是禁用状态 可选项: boolean
        return self.set("disabled", disabled)

        
    def disabledOn(self, disabledOn):
        # 当前表单项是否禁用的条件 可选项: [表达式](../../../docs/concepts/expression)
        return self.set("disabledOn", disabledOn)

        
    def visible(self, visible):
        # 当前表单项是否禁用的条件 可选项: [表达式](../../../docs/concepts/expression)
        return self.set("visible", visible)

        
    def visibleOn(self, visibleOn):
        # 当前表单项是否禁用的条件 可选项: [表达式](../../../docs/concepts/expression)
        return self.set("visibleOn", visibleOn)

        
    def required(self, required):
        # 是否为必填。 可选项: boolean
        return self.set("required", required)

        
    def requiredOn(self, requiredOn):
        # 通过[表达式](../Types.md#表达式)来配置当前表单项是否为必填。 可选项: [表达式](../../../docs/concepts/expression)
        return self.set("requiredOn", requiredOn)

        
    def validations(self, validations):
        # 表单项值格式验证，支持设置多个，多个规则用英文逗号隔开。 可选项: [表达式](../../../docs/concepts/expression)
        return self.set("validations", validations)

        
    def validateApi(self, validateApi):
        # 表单校验接口 可选项: [表达式](../../../docs/types/api)
        return self.set("validateApi", validateApi)

        
    def autoFill(self, autoFill):
        # 数据录入配置，自动填充或者参照录入 可选项: [SchemaNode](../../docs/types/schemanode)
        return self.set("autoFill", autoFill)

        
    def static(self, static):
        # `2.4.0` 当前表单项是否是静态展示，目前支持静[支持静态展示的表单项](#支持静态展示的表单项) 可选项: boolean
        return self.set("static", static)

        
    def staticClassName(self, staticClassName):
        # `2.4.0` 静态展示时的类名 可选项: string
        return self.set("staticClassName", staticClassName)

        
    def staticLabelClassName(self, staticLabelClassName):
        # `2.4.0` 静态展示时的 Label 的类名 可选项: string
        return self.set("staticLabelClassName", staticLabelClassName)

        
    def staticInputClassName(self, staticInputClassName):
        # `2.4.0` 静态展示时的 value 的类名 可选项: string
        return self.set("staticInputClassName", staticInputClassName)

        
    def staticSchema(self, staticSchema):
        # `2.4.0` 自定义静态展示方式 可选项: [SchemaNode](../../docs/types/schemanode)
        return self.set("staticSchema", staticSchema)

        