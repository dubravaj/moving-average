# implementation of moving average computation for streaming data
# based on https://nestedsoftware.com/2018/03/20/calculating-a-moving-average-on-streaming-data-5a7k.22879.html

# this simple approach uses every new incoming value to recalculate the average value

from dataclasses import dataclass, field
import random
import statistics


@dataclass
class MovingAverageProvider:
    count: int = field(default=0)
    average: float = field(default=0)

    def update_mean(self, new_value: int) -> None:
        """Calcute new average for new incoming value
        Example for int data
        """
        self.count += 1  # update total number of samples
        difference = (new_value - self.average) / self.count

        # update moving average
        self.average += difference

    def get_mean(self) -> float:
        return self.average


if __name__ == "__main__":
    sample_data = random.sample(range(0, 100), 100)
    print(f"Sample data: {sample_data}")
    print(f"Built-in mean: {statistics.mean(sample_data)}")

    mean_provider = MovingAverageProvider()
    for sample in sample_data:
        mean_provider.update_mean(sample)

    print(f"Moving average (mean): {mean_provider.get_mean()}")
