using NSubstitute;
using Library.ApplicationCore;
using Library.ApplicationCore.Entities;
using Library.Infrastructure.Data;
using Microsoft.Extensions.Configuration;

namespace UnitTests.Infrastructure.JsonLoanRepositoryTests;

public class GetLoanTest
{
    private readonly ILoanRepository _mockLoanRepository;
    private readonly JsonLoanRepository _jsonLoanRepository;
    private readonly IConfiguration _configuration;
    private readonly JsonData _jsonData;

    public GetLoanTest()
    {
        _mockLoanRepository = Substitute.For<ILoanRepository>();
        
        _configuration = new ConfigurationBuilder()
            .AddInMemoryCollection(new Dictionary<string, string>
            {
                {"JsonPaths:Authors", Path.Combine("..", "..", "..", "..", "..", "src", "Library.Console", "Json", "Authors.json")},
                {"JsonPaths:Books", Path.Combine("..", "..", "..", "..", "..", "src", "Library.Console", "Json", "Books.json")},
                {"JsonPaths:BookItems", Path.Combine("..", "..", "..", "..", "..", "src", "Library.Console", "Json", "BookItems.json")},
                {"JsonPaths:Patrons", Path.Combine("..", "..", "..", "..", "..", "src", "Library.Console", "Json", "Patrons.json")},
                {"JsonPaths:Loans", Path.Combine("..", "..", "..", "..", "..", "src", "Library.Console", "Json", "Loans.json")}
            }!)
            .Build();
        
        _jsonData = new JsonData(_configuration);
        _jsonLoanRepository = new JsonLoanRepository(_jsonData);
    }

    [Fact(DisplayName = "JsonLoanRepository.GetLoan: Returns loan when loan ID is found")]
    public async Task GetLoan_ReturnsLoanWhenIdFound()
    {
        // Arrange
        var loanId = 1;
        var expectedLoan = LoanFactory.CreateCurrentLoanForPatron(PatronFactory.CreateCurrentPatron());
        expectedLoan.Id = loanId;
        _mockLoanRepository.GetLoan(loanId).Returns(expectedLoan);

        // Act
        var actualLoan = await _jsonLoanRepository.GetLoan(loanId);

        // Assert
        Assert.NotNull(actualLoan);
        Assert.Equal(loanId, actualLoan.Id);
    }
    [Fact(DisplayName = "JsonLoanRepository.GetLoan: Returns null when loan ID is not found")]
    public async Task GetLoan_ReturnsNullWhenLoanIdIsNotFound()
    {
        // Arrange
        var loanId = 999; // Use a loan ID that does not exist in the Loans.json file
        var expectedLoan = new Loan { Id = loanId, BookItemId = 101, PatronId = 202, LoanDate = DateTime.Now, DueDate = DateTime.Now.AddDays(14) };
        _mockLoanRepository.GetLoan(loanId).Returns(expectedLoan);

        // Act
        var actualLoan = await _jsonLoanRepository.GetLoan(loanId);

        // Assert
        Assert.Null(actualLoan);
    }
}

