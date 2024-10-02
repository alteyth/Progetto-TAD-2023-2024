module blink(
    input clk,
    output reg [7:0] led,
    input wire [15:0] sw
);
reg [32:0] counter;
always @(posedge clk) begin
    if(sw[0]) begin
        led[0] <= counter[25];
        counter <= counter + 1;
    end else
        led[0] <= 0;
    
end
endmodule