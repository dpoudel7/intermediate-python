from collections import OrderedDict

# Example: Data Transformation Pipeline
class TransformationPipeline(OrderedDict):
    def add_step(self, name, transform_func):
        self[name] = transform_func
    
    def process(self, data):
        for step_name, transform in self.items():
            print(f"Applying {step_name}...")
            data = transform(data)
        return data

pipeline = TransformationPipeline()
pipeline.add_step('normalize', lambda x: x.lower())
pipeline.add_step('clean', lambda x: x.strip())
result = pipeline.process("  SAMPLE DATA  ")
print("\nPipeline Result:", result)