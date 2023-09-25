from metaflow import FlowSpec, step


class FirstFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.end)

    @step
    def end(self):
        print("Flow is done!")


if __name__ == "__main__":
    FirstFlow()
